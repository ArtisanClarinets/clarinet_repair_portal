import frappe
import unittest

class TestCustomerInstrumentProfile(unittest.TestCase):
    def test_create_instrument_profile(self):
        customer = frappe.get_value("Customer", {}, "name")
        doc = frappe.get_doc({
            "doctype": "Customer Instrument Profile",
            "customer": customer,
            "instrument_type": "Clarinet",
            "serial_number": "XYZ456"
        }).insert()
        self.assertEqual(doc.customer, customer)