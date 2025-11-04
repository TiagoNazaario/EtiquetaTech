// Gráfico de Vendas
const ctxVendas = document.getElementById('chartVendas').getContext('2d');
new Chart(ctxVendas, {
  type: 'bar',
  data: {
<<<<<<< HEAD
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
=======
    labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    datasets: [{
      label: 'Vendas (R$)',
      data: [1200, 1900, 3000, 5000, 2300, 3200],
      borderWidth: 1,
      backgroundColor: '#007bff'
    }]
>>>>>>> ab648a7fb326d4ac050e1892ccc1f66e1667bb29
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

<<<<<<< HEAD
// Função para gerar uma cor aleatória em formato RGB
function gerarCorAleatoria() {
  const r = Math.floor(Math.random() * 256);
  const g = Math.floor(Math.random() * 256);
  const b = Math.floor(Math.random() * 256);
  return `rgb(${r}, ${g}, ${b})`;
}

// Gera um array de cores com base no número de produtos
const coresAleatorias = produtosLabels.map(() => gerarCorAleatoria());

=======
>>>>>>> ab648a7fb326d4ac050e1892ccc1f66e1667bb29
// Gráfico dos Produtos mais Vendidos
const ctxProdutos = document.getElementById('chartProdutos').getContext('2d');
new Chart(ctxProdutos, {
  type: 'pie',
  data: {
<<<<<<< HEAD
    labels: produtosLabels,
    datasets: [{
      label: 'Produtos mais vendidos',
      data: produtosData,
      backgroundColor: coresAleatorias, // usa o array gerado
      hoverOffset: 4
    }]
  }
});
=======
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
>>>>>>> ab648a7fb326d4ac050e1892ccc1f66e1667bb29
