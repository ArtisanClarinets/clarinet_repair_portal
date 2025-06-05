# Copyright (c) 2025, MRW Artisan Instruments and contributors
# See license.txt

import frappe
import unittest
from frappe.tests.utils import FrappeTestCase
from frappe.utils import nowdate

class TestRepairRequest(FrappeTestCase):

    def setUp(self):
        self.customer = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": "Test Customer"
        }).insert(ignore_permissions=True)

        self.user = frappe.get_doc({
            "doctype": "User",
            "email": "tech@example.com",
            "first_name": "Tech",
            "roles": [{"role": "Repair Technician"}]
        }).insert(ignore_permissions=True)

    def test_basic_creation(self):
        doc = frappe.get_doc({
            "doctype": "Repair Request",
            "customer": self.customer.name,
            "instrument_type": "A",
            "repair_type": "Maintenance",
            "repair_technician": self.user.name
        })
        doc.insert()
        self.assertTrue(doc.name.startswith("RR-"))

    def test_required_fields_validation(self):
        doc = frappe.get_doc({
            "doctype": "Repair Request",
            "customer": self.customer.name,
            "instrument_type": "A",
            "repair_type": "Customization"
        })
        with self.assertRaises(frappe.ValidationError):
            doc.insert()

    def test_on_submit_creates_inspection(self):
        doc = frappe.get_doc({
            "doctype": "Repair Request",
            "customer": self.customer.name,
            "instrument_type": "B♭",
            "repair_type": "Maintenance",
            "repair_technician": self.user.name
        })
        doc.insert()
        doc.submit()

        inspection = frappe.get_doc("Repair Inspection", {"repair_request": doc.name})
        self.assertEqual(inspection.instrument_type, "B♭")
        self.assertEqual(inspection.repair_request, doc.name)

    def test_status_update(self):
        doc = frappe.get_doc({
            "doctype": "Repair Request",
            "customer": self.customer.name,
            "instrument_type": "E♭",
            "repair_type": "Overhaul",
            "repair_technician": self.user.name
        })
        doc.insert()
        from clarinet_repair_portal.clarinet_repair_portal.doctype.repair_request.repair_request import update_status
        update_status(doc.name, "In Progress")
        doc.reload()
        self.assertEqual(doc.repair_status, "In Progress")