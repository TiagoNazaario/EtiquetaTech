// Gráfico de Vendas
const ctxVendas = document.getElementById('chartVendas').getContext('2d');
new Chart(ctxVendas, {
  type: 'bar',
  data: {
    labels: meses, 
    datasets: [{
      label: 'Vendas (R$)',
      data: valores,
      borderWidth: 1,
      backgroundColor: '#007bff'
    }]
  },
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});

// Gráfico de Pedidos
const ctxClientes = document.getElementById('chartClientes').getContext('2d');
new Chart(ctxClientes, {
  type: 'line',
  data: {
    labels: meses,
    datasets: [{
      label: 'Novos Clientes',
      data: [5, 8, 4, 6, 9, 7, 3],
      borderColor: '#28a745',
      fill: false,
      tension: 0.3
    }]
  }
});

// Função para gerar uma cor aleatória 
function gerarCorAleatoria() {
  const r = Math.floor(Math.random() * 256);
  const g = Math.floor(Math.random() * 256);
  const b = Math.floor(Math.random() * 256);
  return `rgb(${r}, ${g}, ${b})`;
}


const coresAleatorias = produtosLabels.map(() => gerarCorAleatoria());

// Gráfico dos Produtos mais Vendidos
const ctxProdutos = document.getElementById('chartProdutos').getContext('2d');
new Chart(ctxProdutos, {
  type: 'pie',
  data: {
    labels: produtosLabels,
    datasets: [{
      label: 'Produtos Vendidos',
      data: produtosData && produtosData.length > 0 ? produtosData : [1],
      backgroundColor: coresAleatorias, 
      hoverOffset: 25
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'right'
      },
      title: {
        display: true,
        text: 'Top 10 Produtos Mais Vendidos'
      }
    }
  }
});

