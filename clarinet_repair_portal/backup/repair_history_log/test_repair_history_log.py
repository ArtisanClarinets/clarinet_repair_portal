import frappe
import unittest
from frappe.utils import today

class TestRepairHistoryLog(unittest.TestCase):
    def test_insert_repair_log(self):
        log = frappe.get_doc({
            "doctype": "Repair History Log",
            "repair_event_date": today(),
            "summary": "Cork replaced on upper joint."
        }).insert()
        self.assertIn("Cork", log.summary)