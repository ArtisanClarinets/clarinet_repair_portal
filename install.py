# install.py

import frappe
import json
import os


def after_install():
    # Validate fixture JSONs for missing 'name' fields
    fixtures_path = "/opt/frappe/erpnext-bench/apps/clarinet_repair_portal/clarinet_repair_portal/fixtures"
    for root, dirs, files in os.walk(fixtures_path):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = json.load(f)
                        if isinstance(content, list):
                            for entry in content:
                                if "name" not in entry:
                                    print(f"❌ Missing 'name' in: {file_path}")
                                    print(entry)
                except Exception as e:
                    print(f"⚠️ Error reading {file_path}: {e}")

    # Workspace initialization (optional)
    if not frappe.db.exists("Workspace", "Clarinet Repair Portal"):
        content = json.dumps([
            {
                "label": "Documents",
                "type": "card",
                "links": [
                    {"type": "DocType", "name": "Repair Request"},
                    {"type": "DocType", "name": "Repair Inspection"},
                    {"type": "DocType", "name": "Clarinet Anatomy Condition"},
                    {"type": "DocType", "name": "Instrument Preset Template"},
                    {"type": "DocType", "name": "Instrument Tracker"},
                    {"type": "DocType", "name": "Repair Log Entry"}
                ]
            },
            {
                "label": "Reports",
                "type": "card",
                "links": [
                    {"type": "Report", "name": "Repair Status Overview"},
                    {"type": "Report", "name": "Technician Time Summary"},
                    {"type": "Report", "name": "Customer Repair History"}
                ]
            },
            {
                "label": "Tools & QA",
                "type": "card",
                "links": [
                    {"type": "DocType", "name": "Repair QA Checklist"},
                    {"type": "DocType", "name": "Repair Pads Used"},
                    {"type": "DocType", "name": "Tool Usage Log"},
                    {"type": "DocType", "name": "Ultrasonic Cleaning Log"}
                ]
            }
        ])

        doc = frappe.get_doc({
            "doctype": "Workspace",
            "module": "clarinet_repair_portal",
            "workspace_name": "Clarinet Repair Portal",
            "label": "Clarinet Repair Portal",
            "title": "Clarinet Repair Portal",
            "public": 1,
            "icon": "quality-3",
            "is_standard": 1,
            "content": content
        })
        doc.insert(ignore_permissions=True)
        frappe.db.commit()