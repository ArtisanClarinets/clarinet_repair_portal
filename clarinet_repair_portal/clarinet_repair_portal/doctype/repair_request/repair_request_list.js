// repair_request_list.js
frappe.listview_settings['Repair Request'] = {
  add_fields: [
    'customer', 'repair_status', 'priority', 'repair_technician', 'requested_completion_date'
  ],
  get_indicator: function (doc) {
    if (doc.repair_status === 'Completed') {
      return [__('Completed'), 'green', 'repair_status,=,Completed'];
    } else if (doc.repair_status === 'In Progress') {
      return [__('In Progress'), 'orange', 'repair_status,=,In Progress'];
    } else {
      return [__('Pending'), 'gray', 'repair_status,=,Pending'];
    }
  }
};