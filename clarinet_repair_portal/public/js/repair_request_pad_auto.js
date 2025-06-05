// Auto-populate Repair Pads Used based on Clarinet Pad Library
doc_events = {
  'Repair Request': {
    refresh: function (frm) {
      if (frm.doc.instrument_model && frm.doc.repair_pads_used?.length === 0) {
        frappe.call({
          method: 'frappe.client.get_list',
          args: {
            doctype: 'Clarinet Pad Library',
            filters: {instrument_model: frm.doc.instrument_model},
            fields: ['name']
          },
          callback: function (res) {
            if (res.message.length > 0) {
              let lib_name = res.message[0].name;
              frappe.call({
                method: 'frappe.client.get',
                args: {
                  doctype: 'Clarinet Pad Library',
                  name: lib_name
                },
                callback: function (r) {
                  if (r.message.pads?.length > 0) {
                    r.message.pads.forEach(pad => {
                      frm.add_child('repair_pads_used', {
                        pad_location: pad.pad_location,
                        pad_size: pad.pad_size,
                        pad_material: pad.pad_material,
                        source: 'Library'
                      });
                    });
                    frm.refresh_field('repair_pads_used');
                  }
                }
              });
            }
          }
        });
      }
    }
  }
};