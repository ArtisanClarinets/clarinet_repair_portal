import frappe
import json
import os
from datetime import datetime

def serialize(obj):
    if isinstance(obj, dict):
        return {k: serialize(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [serialize(v) for v in obj]
    elif isinstance(obj, datetime):
        return obj.isoformat()
    else:
        return obj

def run():
    doc = frappe.get_doc("DocType", "Roadmap Feature")
    data = serialize(doc.as_dict())
    path = os.path.join(frappe.get_app_path("clarinet_repair_portal"), "fixtures", "roadmap_feature.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump([data], f, indent=2, sort_keys=True)
    print("Fixture written to:", path)