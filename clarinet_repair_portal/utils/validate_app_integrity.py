import frappe
from frappe.model.meta import get_meta

def validate_clarinet_repair_portal():
    broken_links = []
    missing_doctypes = []
    all_custom_doctypes = frappe.get_all("DocType", filters={"module": "Clarinet Repair Portal"})

    for doctype_record in all_custom_doctypes:
        doctype_name = doctype_record.name
        try:
            meta = get_meta(doctype_name)
            for df in meta.fields:
                if df.fieldtype == "Link" and df.options:
                    if not frappe.db.exists("DocType", df.options):
                        broken_links.append((doctype_name, df.fieldname, df.options))
        except Exception as e:
            missing_doctypes.append((doctype_name, str(e)))

    print("Broken Link Fields:")
    for entry in broken_links:
        print(f" - Doctype: {entry[0]}, Field: {entry[1]}, Links to Missing: {entry[2]}")

    print("\nUnloaded or Invalid Doctypes:")
    for entry in missing_doctypes:
        print(f" - {entry[0]}: {entry[1]}")

if __name__ == "__main__":
    frappe.init(site="yoursite")
    frappe.connect()
    validate_clarinet_repair_portal()
    frappe.destroy()