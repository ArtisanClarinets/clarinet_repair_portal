import frappe

def run():
    features = [
        ("Instrument Condition History", "Technician Tools"),
        ("Technician Dashboard", "Technician Tools"),
        ("Auto Repair Estimator", "AI Tools"),
        ("Tagging System", "Core Module"),
        ("Customer Feedback Tracker", "Customer Portal"),
        ("Serialized Instrument Tracker", "Inventory"),
        ("KPI Reports", "Reporting"),
        ("Live SVG Pad Mapper", "Technician Tools"),
        ("Repair Timeline", "Technician Tools"),
        ("Time Logger", "Technician Tools"),
        ("Mobile Tech View", "Customer Portal"),
        ("Parts Recommendation Engine", "AI Tools"),
        ("QA Wizard", "Automation"),
        ("Audio Diagnostic Uploader", "Integration"),
        ("QR Labels", "Inventory"),
        ("Calibration Charts", "Technician Tools")
    ]

    for name, category in features:
        if not frappe.db.exists("Roadmap Feature", {"feature_name": name}):
            doc = frappe.get_doc({
                "doctype": "Roadmap Feature",
                "feature_name": name,
                "category": category,
                "is_planned": 1,
                "is_implemented": 0
            })
            doc.insert(ignore_permissions=True)
    frappe.db.commit()