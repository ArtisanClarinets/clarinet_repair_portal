import frappe
from frappe import _
from frappe.utils import getdate

def get_context(context):
    serial_number = frappe.form_dict.serial_number
    if not serial_number:
        context.logs = []
        context.title = "Missing Serial Number"
        return

    instrument = frappe.get_doc("Instrument Tracker", {"serial_number": serial_number})
    context.title = f"Condition History for {serial_number}"
    context.serial_number = serial_number
    context.model = instrument.model
    context.owner = instrument.owner
    context.logs = [
        {
            "log_date": log.log_date,
            "summary": log.condition_summary
        } for log in instrument.condition_logs
    ]