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

@frappe.whitelist()
def update_status(docname, status):
    doc = frappe.get_doc("Repair Request", docname)
    old_status = doc.repair_status
    doc.repair_status = status
    doc.save()
    frappe.db.commit()

    if old_status != status:
        doc.add_comment("Comment", text=f"Status changed from {old_status} to {status} by {frappe.session.user}")