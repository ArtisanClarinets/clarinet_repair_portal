import frappe
from frappe.model.document import Document

class RepairRequest(Document):
    def on_submit(self):
        inspection = frappe.new_doc("Repair Inspection")
        inspection.repair_request = self.name
        inspection.inspection_date = frappe.utils.today()
        inspection.inspector = frappe.session.user
        inspection.insert(ignore_permissions=True)
        frappe.msgprint(f"Repair Inspection {inspection.name} created.")

@frappe.whitelist()
def update_status(docname, status):
    doc = frappe.get_doc("Repair Request", docname)
    doc.repair_status = status
    doc.save()
    frappe.db.commit()