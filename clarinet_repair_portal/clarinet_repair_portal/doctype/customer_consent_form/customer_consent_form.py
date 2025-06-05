import frappe
from frappe.model.document import Document

class CustomerConsentForm(Document):
    def validate(self):
        if not self.signature:
            frappe.throw("Signature is required before submission.")
        if not self.date:
            frappe.throw("Consent date must be provided.")