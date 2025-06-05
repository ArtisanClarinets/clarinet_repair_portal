import frappe

def insert_test_customer():
    if not frappe.db.exists("Customer", "Test Customer"):
        doc = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": "Test Customer",
            "customer_type": "Individual"
        })
        doc.insert()

