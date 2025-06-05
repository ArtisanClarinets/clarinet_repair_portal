import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class CustomerInstrumentProfile(Document):
    def autoname(self):
        if self.customer and self.serial_number:
            self.name = f"{self.customer}-{self.serial_number}"
        else:
            self.name = f"CIP-{frappe.generate_hash(length=8)}"

    def validate(self):
        if not self.model:
            frappe.throw("Instrument model is required.")
        if not self.serial_number:
            frappe.throw("Instrument serial must be entered.")