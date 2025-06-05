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
  }
});