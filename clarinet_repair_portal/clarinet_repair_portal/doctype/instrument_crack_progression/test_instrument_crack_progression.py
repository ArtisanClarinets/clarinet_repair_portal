import frappe
import unittest

class TestInstrumentCrackProgression(unittest.TestCase):
    def test_creation(self):
        frappe.get_doc({
            "doctype": "Customer",
            "customer_name": "Test Customer"
        }).insert(ignore_if_duplicate=True)

        parent = frappe.get_doc({
            "doctype": "Repair Request",
            "repair_id": "UNIT-TEST-ICP",
            "customer": "Test Customer",
            "instrument_type": "B♭"
        }).insert()

        parent.append("instrument_crack_progressions", {
            "crack_location": "Tenon",
            "notes": "Inserted via test"
        })
        parent.save()

        self.assertEqual(parent.instrument_crack_progressions[0].crack_location, "Tenon")
