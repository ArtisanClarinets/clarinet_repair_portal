from . import __version__ as app_version

app_name = "clarinet_repair_portal"
app_title = "Clarinet Repair Portal"
app_publisher = "MRW Artisan Instruments"
app_description = "Technician-focused clarinet repair workflow portal"
app_email = "support@artisanclarinets.com"
app_license = "MIT"

# Ensure autoname for Repair Request is enforced during reload

def after_migrate():
    import frappe
    frappe.db.set_value("DocType", "Repair Request", "autoname", "field:name")
    
fixtures = [
    "Custom Field",
    "Property Setter",
    "Workspace",
    "DocType",
    "Page",
    "Client Script",
    "Server Script",
    "Custom DocPerm",
    "Translation",
    "Role",
    "Role Profile",
    "Print Format",
    "Report",
    "Dashboard",
    "Module Def",
    "Custom Role"    ]