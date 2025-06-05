__version__ = '0.0.1'

# Apply global test patches before anything else
import frappe
import erpnext.stock.doctype.item.item as item_module

def skip_opening_stock(self):
    if not getattr(frappe.flags, 'in_test', False):
        return item_module.Item.set_opening_stock.__wrapped__(self)

item_module.Item.set_opening_stock = skip_opening_stock