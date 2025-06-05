import frappe
import erpnext.stock.doctype.item.item as item_module

# Skip opening stock setup during test context
def patched_set_opening_stock(self):
    if not getattr(frappe.flags, 'in_test', False):
        return item_module.Item.set_opening_stock.__wrapped__(self)

item_module.Item.set_opening_stock = patched_set_opening_stock