import frappe
import unittest

class TestTechnicianTaskQueue(unittest.TestCase):
    def test_creation(self):
        doc = frappe.get_doc({
            "doctype": "Technician Task Queue",
            "task_id": "T-001",
            "repair_request": "REQ-001",
            "technician": "tech@example.com"
        })
        doc.insert()
        self.assertEqual(doc.task_id, "T-001")