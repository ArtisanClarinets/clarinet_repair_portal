import frappe
import unittest
from frappe.utils import nowdate

class TestToolUsageLog(unittest.TestCase):
    def test_create_tool_usage(self):
        log = frappe.get_doc({
            "doctype": "Tool Usage Log",
            "tool": "Pad Slick",
            "usage_date": nowdate(),
            "task_description": "Level tonehole"
        }).insert()
        self.assertEqual(log.tool, "Pad Slick")