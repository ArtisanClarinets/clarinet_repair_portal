frappe.ui.form.on('Repair Inspection', {
  onload(frm) {
    frm.fields_dict.interactive_anatomy_image.$wrapper.html(`
      <div id="anatomy-svg-wrapper">
        <object type="image/svg+xml" data="/assets/clarinet_repair_portal/images/clarinet_anatomy.svg" id="clarinet-anatomy" style="width:100%; height:auto;"></object>
      </div>
    `);

    setTimeout(() => {
      const svgObj = document.getElementById("clarinet-anatomy");
      if (!svgObj || !svgObj.contentDocument) return;

      const svgDoc = svgObj.contentDocument;
      svgDoc.querySelectorAll("[data-part-id]").forEach(el => {
        el.style.cursor = "pointer";
        el.addEventListener("click", () => {
          const part = el.getAttribute("data-part-id");
          let new_row = frm.add_child("condition_checklist", {
            clarinet_part: part
          });
          frm.refresh_field("condition_checklist");
        });
      });
    }, 1000);
  }
});