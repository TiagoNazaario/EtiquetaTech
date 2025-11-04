// Gráfico de Vendas
const ctxVendas = document.getElementById('chartVendas').getContext('2d');
new Chart(ctxVendas, {
  type: 'bar',
  data: {
    labels: meses, // ← vindo do Flask
    datasets: [{
      label: 'Vendas (R$)',
      data: valores, // ← vindo do Flask
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

// Função para gerar uma cor aleatória em formato RGB
function gerarCorAleatoria() {
  const r = Math.floor(Math.random() * 256);
  const g = Math.floor(Math.random() * 256);
  const b = Math.floor(Math.random() * 256);
  return `rgb(${r}, ${g}, ${b})`;
}

// Gera um array de cores com base no número de produtos
const coresAleatorias = produtosLabels.map(() => gerarCorAleatoria());

// Gráfico dos Produtos mais Vendidos
const ctxProdutos = document.getElementById('chartProdutos').getContext('2d');
new Chart(ctxProdutos, {
  type: 'pie',
  data: {
    labels: produtosLabels,
    datasets: [{
      label: 'Produtos mais vendidos',
      data: produtosData,
      backgroundColor: coresAleatorias, // usa o array gerado
      hoverOffset: 4
    }]
  }
});
