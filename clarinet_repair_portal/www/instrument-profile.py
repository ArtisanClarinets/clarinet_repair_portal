import frappe
from frappe.www.page_renderers.template_page import TemplatePage

def get_context(context):
    if not frappe.session.user or frappe.session.user == "Guest":
        frappe.throw("Login required to access instrument profile.")

    customer = frappe.db.get_value("Contact", {"email_id": frappe.session.user}, "name")
    instruments = frappe.get_all("Instrument", filters={"customer": customer}, fields=[
        "name", "instrument_type", "manufacturer", "model", "serial_number", "year_of_manufacture", "body_photo"
    ])

    context.no_cache = True
    context.instruments = instruments
    return context