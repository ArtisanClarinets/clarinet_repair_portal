import frappe
from frappe.model.document import Document

class RepairLogEntry(Document):
    def validate(self):
        if not self.repair_step:
            frappe.throw("Repair Step is required.")
        if not self.technician:
            frappe.throw("Technician must be specified.")
        if not self.timestamp:
            frappe.throw("Timestamp must be set.")