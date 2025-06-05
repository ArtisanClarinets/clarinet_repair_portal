frappe.ui.form.on('Instrument Tracker', {
  launch_repair_request: function(frm) {
    frappe.call({
      method: 'frappe.client.insert',
      args: {
        doc: {
          doctype: 'Repair Request',
          customer: frm.doc.owner,
          serial_number: frm.doc.serial_number,
          instrument_tracker: frm.doc.name
        }
      },
      callback: function(r) {
        if (!r.exc) {
          frappe.msgprint(__('Repair Request created: ') + r.message.name);
          frappe.set_route('Form', 'Repair Request', r.message.name);
        }
      }
    });
  }
});