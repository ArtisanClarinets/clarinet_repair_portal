frappe.ui.form.on('Repair QA Step', {
  status: function (frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    if (row.status && row.status !== 'Pending' && row.auto_timestamp) {
      frappe.model.set_value(cdt, cdn, 'performed_by', frappe.session.user);
      frappe.model.set_value(cdt, cdn, 'timestamp', frappe.datetime.now_datetime());
    }
  }
});

frappe.ui.form.on('QA Log', {
  status: function (frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    if (row.status && row.status !== 'Pending') {
      frappe.model.set_value(cdt, cdn, 'checked_by', frappe.session.user);
      frappe.model.set_value(cdt, cdn, 'date_checked', frappe.datetime.get_today());
    }
  }
});