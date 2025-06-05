import frappe
import unittest

class TestBootstrapData(unittest.TestCase):
    def test_create_required_fixtures(self):
        # Ensure UOM exists
        if not frappe.db.exists("UOM", "Nos"):
            frappe.get_doc({"doctype": "UOM", "uom_name": "Nos"}).insert()

        # Create Customer
        if not frappe.db.exists("Customer", "Test Customer"):
            frappe.get_doc({
                "doctype": "Customer",
                "customer_name": "Test Customer",
                "customer_type": "Individual"
            }).insert()

        # Create Technician (as User)
        if not frappe.db.exists("User", "tech@example.com"):
            user = frappe.get_doc({
                "doctype": "User",
                "email": "tech@example.com",
                "first_name": "Technician",
            })
            user.insert()
            user.add_roles("Employee")

        # Create Instrument manually
        if not frappe.db.exists("Instrument", "TEST123"):
            doc = frappe.get_doc({
                "doctype": "Instrument",
                "instrument_id": "TEST123",
                "instrument_type": "Clarinet",
                "serial_number": "SN123",
                "naming_series": "INST-"
            })
            doc.name = "TEST123"
            doc.insert()

        # Create Instrument Tracker
        if not frappe.db.exists("Instrument Tracker", {"instrument": "TEST123"}):
            frappe.get_doc({
                "doctype": "Instrument Tracker",
                "instrument": "TEST123",
                "location": "Storage Room"
            }).insert()

        # Create Repair Request
        if not frappe.db.exists("Repair Request", {"instrument": "TEST123"}):
            tracker = frappe.get_value("Instrument Tracker", {"instrument": "TEST123"}, "name")
            frappe.get_doc({
                "doctype": "Repair Request",
                "customer": "Test Customer",
                "instrument": "TEST123",
                "instrument_tracker": tracker
            }).insert()

        # Create Preset Template with required fields
        if not frappe.db.exists("Instrument Preset Template", "Clarinet Setup A"):
            frappe.get_doc({
                "doctype": "Instrument Preset Template",
                "template_name": "Clarinet Setup A",
                "estimated_repair_duration": 60
            }).insert()