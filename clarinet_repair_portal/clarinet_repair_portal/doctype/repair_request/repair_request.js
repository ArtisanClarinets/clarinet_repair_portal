frappe.ui.form.on("Repair Request", {
  refresh(frm) {
    if (!frm.is_new()) {
      if (frm.doc.repair_status !== "Completed") {
        frm.add_custom_button("Start Repair", () => {
          frappe.call({
            method: "clarinet_repair_portal.clarinet_repair_portal.doctype.repair_request.repair_request.update_status",
            args: {
              docname: frm.doc.name,
              status: "In Progress"
            },
            callback: () => frm.reload()
          });
        }, "Actions");

        frm.add_custom_button("Awaiting Parts", () => {
          frappe.call({
            method: "clarinet_repair_portal.clarinet_repair_portal.doctype.repair_request.repair_request.update_status",
            args: {
              docname: frm.doc.name,
              status: "Awaiting Parts"
            },
            callback: () => frm.reload()
          });
        }, "Actions");
      }

      if (frm.doc.repair_status === "In Progress") {
        frm.add_custom_button("Complete Repair", () => {
          frappe.call({
            method: "clarinet_repair_portal.clarinet_repair_portal.doctype.repair_request.repair_request.update_status",
            args: {
              docname: frm.doc.name,
              status: "Completed"
            },
            callback: () => frm.reload()
          });
        }, "Actions");
      }
    }
  },

  customer(frm) {
    if (frm.doc.customer) {
      frappe.db.get_list("Instrument", {
        filters: { customer: frm.doc.customer },
        fields: ["name", "instrument_type", "brand", "model"],
        limit: 50
      }).then(instruments => {
        if (instruments.length > 0) {
          frappe.prompt([
            {
              label: "Select Instrument",
              fieldname: "instrument",
              fieldtype: "Link",
              options: "Instrument",
              reqd: true
            }
          ], (values) => {
            frm.set_value("instrument", values.instrument);
          }, "Customer Instruments", "Choose");
        }
      });
    }
  },

  repair_type(frm) {
    if (frm.doc.repair_type === "Customization" && (!frm.doc.requested_services || frm.doc.requested_services.length === 0)) {
      frappe.show_alert("Customization selected: Please add at least one requested service.", 5);
    }
  }
});