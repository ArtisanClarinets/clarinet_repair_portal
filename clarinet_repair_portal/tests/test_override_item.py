import frappe
import unittest
from unittest.mock import patch
import erpnext.stock.doctype.item.item as item_module

class TestItemPatch(unittest.TestCase):
    def test_disable_opening_stock(self):
        with patch.object(item_module.Item, "set_opening_stock", lambda self: None):
            doc = frappe.get_doc({
                'doctype': 'Item',
                'item_code': frappe.generate_hash(length=10),
                'item_group': 'All Item Groups',
                'stock_uom': 'Nos',
                'is_stock_item': 1
            })
            doc.insert()
            self.assertEqual(doc.doctype, "Item")
            frappe.delete_doc("Item", doc.name)