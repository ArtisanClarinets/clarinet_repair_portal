import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class PlaytestLog(Document):
    def autoname(self):
        if self.repair_request and self.playtest_type:
            self.name = f"{self.repair_request}-{self.playtest_type}-{nowdate()}"
        else:
            self.name = f"PT-{frappe.generate_hash(length=8)}"

    def validate(self):
        if not self.playtest_type:
            frappe.throw("Playtest Type must be specified.")
        if not self.technician:
            frappe.throw("Technician must be assigned for the playtest log.")