// File: clarinet_repair_portal/public/js/repair_request.js

frappe.ui.form.on('Repair Request', {
    refresh: function(frm) {
        if (!frm.doc.__islocal && frm.doc.docstatus < 2) {
            const actions = [
                { label: "Mark as Inspected", status: "Inspected" },
                { label: "Mark as Quoted", status: "Quoted" },
                { label: "Mark as In Progress", status: "In Progress" },
                { label: "Mark as Completed", status: "Completed" },
            ];

            actions.forEach(action => {
                frm.add_custom_button(__(action.label), function () {
                    frappe.call({
                        method: "clarinet_repair_portal.clarinet_repair_portal.doctype.repair_request.repair_request.update_status",
                        args: {
                            docname: frm.doc.name,
                            status: action.status
                        },
                        callback: function(r) {
                            if (!r.exc) {
                                frappe.msgprint(__('Status updated to {0}', [action.status]));
                                frm.reload_doc();
                            }
                        }
                    });
                }, __("Actions"));
            });
        }
    }
});