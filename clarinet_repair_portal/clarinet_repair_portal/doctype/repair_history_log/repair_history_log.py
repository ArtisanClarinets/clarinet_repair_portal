import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class RepairHistoryLog(Document):
    def validate(self):
        if self.repair_event_date and self.repair_event_date > nowdate():
            frappe.throw("Repair Event Date cannot be in the future.")

        if not self.technician:
            self.technician = frappe.session.user