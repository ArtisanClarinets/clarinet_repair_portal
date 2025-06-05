// instrument_tracker.js
frappe.ui.form.on('Instrument Tracker', {
  launch_repair_request: function(frm) {
    frappe.call({
      method: "frappe.client.insert",
      args: {
        doc: {
          doctype: "Repair Request",
          instrument: frm.doc.name,
          customer: frm.doc.owner,
          instrument_type: frm.doc.instrument_type,
          serial_number: frm.doc.serial_number,
          status: "Open"
        }
      },
      callback: function(response) {
        if (!response.exc && response.message) {
          frappe.msgprint(__('Repair Request Created: {0}', [
            `<a href='/app/repair-request/${response.message.name}'>${response.message.name}</a>`
          ]));
          frappe.set_route("Form", "Repair Request", response.message.name);
        }
      }
    });
  }
});