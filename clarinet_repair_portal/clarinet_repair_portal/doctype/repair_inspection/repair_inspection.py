import frappe
from frappe.model.document import Document

class RepairInspection(Document):
    def on_submit(self):
        history = frappe.new_doc("Repair History Log")
        history.repair_event_date = frappe.utils.today()
        history.related_repair = self.repair_request
        history.repair_type = "Inspection"
        history.summary = self.findings_summary
        history.technician = self.inspector
        history.insert(ignore_permissions=True)
        frappe.msgprint(f"Repair History Log {history.name} created.")