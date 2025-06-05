# File: clarinet_repair_portal/config/repair_request.py

from frappe import _

def get_data():
    return [
        {
            "label": _("Repair Management"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Repair Request",
                    "label": _("Repair Request"),
                    "description": _("Track clarinet repair intake and status"),
                }
            ]
        }
    ]