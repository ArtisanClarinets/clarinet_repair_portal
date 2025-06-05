frappe.ready(() => {
  const logs = {{ logs | tojson | safe }};
  const dates = logs.map(log => log.log_date);
  const summaries = logs.map(log => log.summary);

  const ctx = document.getElementById('timeline-chart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: dates,
      datasets: [{
        label: 'Condition Notes Timeline',
        data: summaries.map((_, i) => i + 1), // dummy y-axis
        borderColor: '#2563eb',
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      plugins: {
        tooltip: {
          callbacks: {
            label: function(context) {
              return summaries[context.dataIndex];
            }
          }
        }
      },
      scales: {
        y: {
          display: false
        }
      }
    }
  });
});