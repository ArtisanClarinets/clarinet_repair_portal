import frappe
import unittest

class TestRepairLogEntry(unittest.TestCase):
    def test_create_log_entry(self):
        log = frappe.get_doc({
            "doctype": "Repair Log Entry",
            "log_type": "Service Note",
            "entry_text": "Adjusted bridge key height."
        }).insert()
        self.assertIn("bridge", log.entry_text.lower())