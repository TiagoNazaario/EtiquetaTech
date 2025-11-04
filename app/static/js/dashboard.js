// Gráfico de Vendas
const ctxVendas = document.getElementById('chartVendas').getContext('2d');
new Chart(ctxVendas, {
  type: 'bar',
  data: {
    labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    datasets: [{
      label: 'Vendas (R$)',
      data: [1200, 1900, 3000, 5000, 2300, 3200],
      borderWidth: 1,
      backgroundColor: '#007bff'
    }]
  }
});

// Gráfico de Clientes
const ctxClientes = document.getElementById('chartClientes').getContext('2d');
new Chart(ctxClientes, {
  type: 'line',
  data: {
    labels: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'],
    datasets: [{
      label: 'Novos Clientes',
      data: [5, 8, 4, 6, 9, 7, 3],
      borderColor: '#28a745',
      fill: false,
      tension: 0.3
    }]
  }
});

// Gráfico dos Produtos mais Vendidos
const ctxProdutos = document.getElementById('chartProdutos').getContext('2d');
new Chart(ctxProdutos, {
  type: 'pie',
  data: {
    labels: ['Item1', 'Item2', 'Item3', 'Item4'],
    datasets: [{
      label: 'Produtos mais vendidos',
      data: [4, 5, 6, 23],
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)',
        'rgba(68, 216, 30, 1)'
      ],
      hoverOffset: 4
    }]
  }
});