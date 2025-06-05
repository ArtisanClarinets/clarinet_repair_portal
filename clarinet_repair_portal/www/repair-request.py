import frappe
from frappe.utils import nowdate
from frappe import _

def get_context(context):
    name = frappe.form_dict.get("name") or frappe.local.form_dict.get("name")
    if not name:
        frappe.throw("Missing Repair Request ID")

    doc = frappe.get_doc("Repair Request", name)

    # Check access rights
    if frappe.session.user != "Guest" and doc.customer:
        customer_email = frappe.db.get_value("Customer", doc.customer, "email_id")
        if frappe.session.user != customer_email:
            frappe.throw("You are not permitted to view this repair.")

    # Handle message post
    if frappe.form_dict.get("subject") and frappe.form_dict.get("content"):
        doc.append("customer_communication_log", {
            "subject": frappe.form_dict.get("subject"),
            "content": frappe.form_dict.get("content"),
            "communication_date": nowdate(),
            "communication_type": "Comment"
        })
        doc.save()
        frappe.msgprint("Message sent.")

    context.doc = doc
    return context