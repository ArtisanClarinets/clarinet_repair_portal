import frappe
from frappe.test_runner import get_dependencies

# Patch get_dependencies to skip NoneType keys during sorting
original_get_dependencies = get_dependencies

def safe_get_dependencies(app):
    deps = original_get_dependencies(app)
    safe_deps = {k: v for k, v in deps.items() if k is not None}
    return dict(sorted(safe_deps.items(), key=lambda x: x[0] or "zzz"))

frappe.test_runner.get_dependencies = safe_get_dependencies