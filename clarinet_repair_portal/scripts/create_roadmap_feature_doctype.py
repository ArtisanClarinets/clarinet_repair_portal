import frappe

def run():
    if not frappe.db.has_table("tabRoadmap Feature"): # type: ignore
        fields = [
            {"fieldname": "feature_name", "label": "Feature Name", "fieldtype": "Data", "reqd": 1},
            {"fieldname": "category", "label": "Feature Category", "fieldtype": "Select", "options": "Core Module\nAutomation\nIntegration\nCustomer Portal\nAI Tools\nReporting\nInventory\nTechnician Tools", "reqd": 1},
            {"fieldname": "is_planned", "label": "Planned?", "fieldtype": "Check", "default": 1},
            {"fieldname": "is_implemented", "label": "Implemented?", "fieldtype": "Check"},
            {"fieldname": "description", "label": "Description", "fieldtype": "Small Text"},
            {"fieldname": "linked_module", "label": "Linked Module", "fieldtype": "Link", "options": "Module Def"},
            {"fieldname": "dev_notes", "label": "Dev Notes", "fieldtype": "Text Editor"}
        ]
        permissions = [{"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1}]
        doc = frappe.get_doc({ # type: ignore
            "doctype": "DocType",
            "name": "Roadmap Feature",
            "module": "clarinet_repair_portal",
            "custom": 1,
            "fields": fields,
            "permissions": permissions
        })
        doc.insert(ignore_permissions=True)
        frappe.db.commit() # type: ignore