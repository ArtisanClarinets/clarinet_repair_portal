frappe.ui.form.on('Repair Intake', {
  refresh: function(frm) {
    if (!frm.is_new() && frm.doc.docstatus === 1) {
      frappe.call({
        method: 'frappe.client.get_list',
        args: {
          doctype: 'Repair Request',
          filters: {
            customer: frm.doc.customer,
            instrument: frm.doc.instrument,
            intake_datetime: frm.doc.intake_datetime
          },
          limit_page_length: 1
        },
        callback: function(r) {
          if (r.message && r.message.length > 0) {
            frm.add_custom_button('View Repair Request', function() {
              frappe.set_route('Form', 'Repair Request', r.message[0].name);
            }, 'Actions');
          }
        }
      });
    }
  }
});