import frappe
import unittest

class TestRepairPadsUsed(unittest.TestCase):
    def test_create_pad_usage(self):
        pad = frappe.get_doc({
            "doctype": "Repair Pads Used",
            "pad_type": "Ferree B17",
            "location": "Upper joint - LH3",
            "notes": "Slightly trimmed to fit."
        }).insert()
        self.assertTrue("trimmed" in pad.notes.lower())