import frappe
from frappe.model.document import Document

class RepairIntake(Document):
    def on_submit(self):
        repair_request = frappe.new_doc("Repair Request")
        repair_request.customer = self.customer
        repair_request.contact_person = self.contact_person
        repair_request.instrument = self.instrument
        repair_request.repair_type = self.repair_type
        repair_request.priority = self.priority
        repair_request.expected_delivery_date = self.desired_completion_date
        repair_request.drop_off_method = self.drop_off_method
        repair_request.description = self.initial_description
        repair_request.intake_datetime = self.intake_datetime
        repair_request.intake_checklist = []

        for item in self.intake_checklist:
            repair_request.append("intake_checklist", {
                "check": item.check,
                "status": item.status,
                "notes": item.notes
            })

        repair_request.insert()
        frappe.msgprint(f"Linked Repair Request created: {repair_request.name}")