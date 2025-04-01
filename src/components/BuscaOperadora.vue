<template>
  <div class="container">
    <h2>Busca de Operadoras de Saúde</h2>
    <div class="search-box">
      <input type="text" v-model="query" placeholder="Digite para pesquisar..." />
      <button @click="buscarOperadora">Buscar</button>
    </div>

    <!-- Exibe a lista de resultados se houver -->
    <ul v-if="resultados.length">
      <li v-for="(item, index) in resultados" :key="index">
        <strong>Nome Fantasia:</strong> {{ item.Nome_Fantasia || 'Não disponível' }} <br>
        <strong>Razão Social:</strong> {{ item.Razao_Social || 'Não disponível' }} <br>
        <strong>CNPJ:</strong> {{ item.CNPJ || 'Não disponível' }} <br>
        <strong>Representante:</strong> {{ item.Representante || 'Não disponível' }} <br>
        <strong>Email:</strong> {{ item.Endereco_eletronico || 'Não disponível' }} <br>
        <strong>Modalidade:</strong> {{ item.Modalidade || 'Não disponível' }} <br>
        <strong>Cidade:</strong> {{ item.Cidade || 'Não disponível' }} <br>
        <strong>Região:</strong> {{ item.Regiao_de_Comercializacao || 'Não disponível' }} <br>
        <hr>
      </li>
    </ul>

    <!-- Exibe mensagem se não houver resultados -->
    <p v-else-if="buscaRealizada && resultados.length === 0">Nenhum resultado encontrado.</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      resultados: [],
      buscaRealizada: false, // Variável para controlar quando a busca foi feita
    };
  },
  methods: {
    async buscarOperadora() {
      if (!this.query) return;
      
      // Marca que a busca foi realizada
      this.buscaRealizada = true;

      try {
        const response = await axios.get(`http://localhost:8000/buscar?nome=${this.query}`);
        console.log("Dados recebidos:", response.data);
        this.resultados = response.data.resultados || [];
      } catch (error) {
        console.error("Erro ao buscar operadoras", error);
      }
    }
  }
};
</script>

<style>
.container {
  text-align: center;
}
.search-box {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 10px;
}
input {
  width: 300px;
  padding: 8px;
  border: none;
  background: black;
  color: white;
}
button {
  background: #bfe0cc;
  padding: 8px 16px;
  border: none;
  cursor: pointer;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ddd;
}
hr {
  border: 0;
  border-top: 1px solid #ddd;
}
</style>
