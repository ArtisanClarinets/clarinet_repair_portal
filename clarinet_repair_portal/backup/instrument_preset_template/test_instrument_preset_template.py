import frappe
import unittest

class TestInstrumentPresetTemplate(unittest.TestCase):
    def test_create_template(self):
        template = frappe.get_doc({
            "doctype": "Instrument Preset Template",
            "template_name": "Standard Bb Clarinet",
            "instrument_type": "B♭ Clarinet",
            "estimated_repair_duration": 5
        }).insert()
        self.assertEqual(template.instrument_type, "B♭ Clarinet")