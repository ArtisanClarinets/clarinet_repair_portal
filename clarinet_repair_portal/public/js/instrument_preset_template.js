frappe.ui.form.on('Instrument Preset Template', {
  auto_apply: function(frm) {
    frappe.call({
      method: 'frappe.client.insert',
      args: {
        doc: {
          doctype: 'Repair Request',
          preset_template: frm.doc.name,
          instrument_type: frm.doc.instrument_type,
          standard_parts_required: frm.doc.standard_parts_required.map(row => ({
            item_code: row.item_code,
            qty: row.qty
          }))
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