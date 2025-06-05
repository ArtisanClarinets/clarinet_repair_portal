import frappe
import unittest

class TestInstrument(unittest.TestCase):
    def test_create_instrument(self):
        customer = frappe.get_value("Customer", {}, "name")
        instrument = frappe.get_doc({
            "doctype": "Instrument",
            "customer": customer,
            "instrument_type": "Clarinet",
            "manufacturer": "Yamaha",
            "model": "CSG III",
            "serial_number": "YCL-123456",
            "year_of_manufacture": 2010
        }).insert()
        self.assertEqual(instrument.instrument_type, "Clarinet")