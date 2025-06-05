// repair_bom.js
frappe.ui.form.on('Repair BOM', {
  refresh(frm) {
    frm.trigger('calculate_total_cost');
  },

  calculate_total_cost(frm) {
    let total = 0;
    (frm.doc.items || []).forEach(item => {
      if (item.qty && item.rate) {
        item.amount = item.qty * item.rate;
        total += item.amount;
      }
    });
    frm.set_value('total_cost', total);
    frm.refresh_field('items');
  },

  items_on_form_rendered(frm) {
    frm.fields_dict.items.grid.wrapper.find('.grid-body').on('change', 'input[data-fieldname="qty"], input[data-fieldname="rate"]', () => {
      frm.trigger('calculate_total_cost');
    });
  }
});