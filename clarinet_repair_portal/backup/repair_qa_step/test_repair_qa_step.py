import frappe
import unittest

class TestRepairQAStep(unittest.TestCase):
    def test_create_qa_step(self):
        step = frappe.get_doc({
            "doctype": "Repair QA Step",
            "step_description": "Verify pad seating",
            "auto_timestamp": 1
        }).insert()
        self.assertTrue(step.step_description.startswith("Verify"))