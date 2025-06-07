# Copyright (c) 2025, MRW Artisan Instruments and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RepairRequest(Document):

    def autoname(self):
        self.name = frappe.model.naming.make_autoname("RR-.YYYY.-.####")

    def validate(self):
        if self.repair_status == "In Progress" and not self.repair_technician:
            frappe.throw("Repair Technician must be assigned before marking status as In Progress.")

        if self.repair_type == "Customization" and not self.requested_services:
            frappe.throw("Customization repairs must include at least one Requested Service.")

        if self.instrument:
            instrument = frappe.get_doc("Instrument", self.instrument)
            if instrument.customer != self.customer:
                frappe.throw("Selected instrument does not belong to the chosen customer.")

        if self.repair_bom and not frappe.db.exists("Repair BOM", self.repair_bom):
            frappe.throw("Repair BOM reference is invalid.")

        if self.repair_steps:
            for step in self.repair_steps:
                if not step.step_code or not step.step_name:
                    frappe.throw("Each Repair Step must have both code and name.")

        if self.repair_log:
            for log in self.repair_log:
                if not log.note or not log.timestamp:
                    frappe.throw("Repair Log Entry must have note and timestamp.")

    def before_submit(self):
        if not self.repair_qa_checklist:
            frappe.throw("QA Checklist must be completed before submitting the repair request.")

        incomplete_steps = [step.qa_check for step in self.repair_qa_checklist if step.result != "Pass"]
        if incomplete_steps:
            frappe.throw(f"All QA steps must be marked 'Pass'. Incomplete: {', '.join(incomplete_steps)}")

    def on_submit(self):
        if not frappe.db.exists("Repair Inspection", {"repair_request": self.name}):
            inspection = frappe.new_doc("Repair Inspection")
            inspection.repair_request = self.name
            inspection.inspection_date = frappe.utils.today()
            inspection.inspector = frappe.session.user
            inspection.instrument_type = self.instrument_type
            inspection.insert(ignore_permissions=True)
            frappe.msgprint(f"Repair Inspection {inspection.name} created.")
        else:
            frappe.msgprint("Repair Inspection already exists for this request.")

    def on_cancel(self):
        inspections = frappe.get_all("Repair Inspection", filters={"repair_request": self.name})
        for insp in inspections:
            doc = frappe.get_doc("Repair Inspection", insp.name)
            doc.cancel()
            frappe.msgprint(f"Linked inspection {doc.name} cancelled.")

    def log_status_change(self, old_status, new_status):
        if old_status != new_status:
            self.add_comment("Comment", text=f"Status changed from {old_status} to {new_status} by {frappe.session.user}")
            if new_status == "Completed":
                self.notify_customer_of_completion()

    def notify_customer_of_completion(self):
        if self.customer:
            email = frappe.db.get_value("Customer", self.customer, "email_id")
            if email:
                message = f"Your instrument repair request {self.name} has been marked as Completed. Thank you."
                frappe.sendmail(
                    recipients=[email],
                    subject="Your Repair is Completed",
                    message=message
                )

@frappe.whitelist()
def update_status(docname, status):
    doc = frappe.get_doc("Repair Request", docname)
    old_status = doc.repair_status
    doc.repair_status = status
    doc.save()
    frappe.db.commit()
    doc.log_status_change(old_status, status)