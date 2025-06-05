import frappe
from frappe.model.document import Document

class InstrumentConditionLog(Document):
    def validate(self):
        if not self.repair_request or not self.technician or not self.inspection_datetime:
            frappe.throw("Repair Request, Technician, and Inspection Datetime are required.")

        if not self.pad_condition and not self.crack_observations:
            frappe.throw("At least one Pad Condition or Crack Observation must be entered before submission.")