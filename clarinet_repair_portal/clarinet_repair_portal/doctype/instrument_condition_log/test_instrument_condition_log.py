import frappe
import unittest

class TestInstrumentConditionLog(unittest.TestCase):
    def test_creation(self):
        frappe.get_doc({
            "doctype": "Customer",
            "customer_name": "Test Customer"
        }).insert(ignore_if_duplicate=True)

        parent = frappe.get_doc({
            "doctype": "Repair Request",
            "repair_id": "UNIT-TEST-ICL",
            "customer": "Test Customer",
            "instrument_type": "Clarinet"
        }).insert()

        parent.append("instrument_condition_logs", {
            "condition": "Cracked Body",
            "notes": "Unit test: Inserted via parent"
        })
        parent.save()

        self.assertEqual(parent.instrument_condition_logs[0].condition, "Cracked Body")
