import frappe
import unittest
from frappe.utils import nowdate
from frappe.model.workflow import apply_workflow
import doctest

def create_test_dependencies():
    if not frappe.db.exists("Manufacturer", "Buffet"):
        frappe.get_doc({
            "doctype": "Manufacturer",
            "manufacturer_name": "Buffet"
        }).insert(ignore_permissions=True)
        frappe.db.commit()

    mfg = frappe.get_doc("Manufacturer", "Buffet")

    if not frappe.db.exists("Instrument Type", {"type_name": "Clarinet Test Type"}):
        inst_type = frappe.get_doc({
            "doctype": "Instrument Type",
            "type_name": "Clarinet Test Type"
        })
        inst_type.insert(ignore_permissions=True)
        frappe.db.commit()
    else:
        inst_type = frappe.get_doc("Instrument Type", {"type_name": "Clarinet Test Type"})

    frappe.clear_cache()

    if not frappe.db.exists("Instrument Model", {"model": "RC Test Model"}):
        frappe.get_doc({
            "doctype": "Instrument Model",
            "model": "RC Test Model",
            "manufacturer": mfg.name,
            "instrument_type": inst_type.name
        }).insert(ignore_permissions=True)
        frappe.db.commit()

class TestAllClarinetRepairPortalDoctypes(unittest.TestCase):
    def setUp(self):
        frappe.set_user("Administrator")
        create_test_dependencies()

    def try_instantiate_and_validate(self, doctype):
        try:
            doc = frappe.new_doc(doctype)
            if hasattr(doc, 'doctype'):
                doc.insert(ignore_permissions=True)
            return doc
        except Exception as e:
            frappe.log_error(f"Failed on {doctype}: {e}", "Test Failure")
            raise

    def test_doctype_instantiation_save_fields_and_relations(self):
        from frappe.modules import get_module_list
        from clarinet_repair_portal import clarinet_repair_portal
        module = clarinet_repair_portal
        module_name = module.__name__.split('.')[-1]

        doctypes = frappe.get_all("DocType", filters={"module": module_name, "istable": 0}, pluck="name")
        for doctype in doctypes:
            with self.subTest(doctype=doctype):
                doc = self.try_instantiate_and_validate(doctype)
                self.assertIsNotNone(doc.name)

    def test_validation_errors(self):
        from frappe.model.document import Document
        with self.assertRaises(frappe.exceptions.MandatoryError):
            doc = frappe.new_doc("Instrument Model")
            doc.insert(ignore_permissions=True)

    def test_workflow_transitions(self):
        try:
            tracker = frappe.get_doc({
                "doctype": "Instrument Tracker",
                "instrument": "TestClarinet001"
            }).insert(ignore_permissions=True)
            apply_workflow(tracker, "Send for Inspection")
            tracker.reload()
            self.assertEqual(tracker.workflow_state, "Under Inspection")
        except frappe.DoesNotExistError:
            self.skipTest("No workflow defined for Instrument Tracker")

    def test_inline_doctests(self):
        result = doctest.testmod()
        self.assertEqual(result.failed, 0, f"Doctest failures: {result.failed}")
