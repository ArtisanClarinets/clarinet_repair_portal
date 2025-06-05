import frappe
import unittest

class TestInstrumentTracker(unittest.TestCase):
    def test_create_tracker(self):
        tracker = frappe.get_doc({
            "doctype": "Instrument Tracker",
            "serial_number": "ABC123",
            "instrument_type": "Clarinet",
            "manufacturer": "Buffet",
            "year_of_manufacture": 1995,
            "owner": frappe.get_value("Customer", {}, "name")
        }).insert()
        self.assertEqual(tracker.instrument_type, "Clarinet")