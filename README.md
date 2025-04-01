# Configurando o Projeto Vue.js + FastAPI

Este projeto utiliza Vue.js para o frontend e FastAPI para o backend. Siga as instruções abaixo para configurar e executar corretamente o ambiente.

## Pré-requisitos
- Node.js instalado
- Python instalado

## Configuração do Frontend (Vue.js)

1. Abra um terminal e instale o Vue CLI globalmente:
   ```sh
   npm install -g @vue/cli
   ```
2. Instale as dependências do projeto:
   ```sh
   npm install
   ```
3. Execute o servidor do frontend:
   ```sh
   npm run serve
   ```

## Configuração do Backend (FastAPI)

1. Em outro terminal, crie um ambiente virtual do Python:
   ```sh
   python -m venv venv
   ```
2. Ative o ambiente virtual:
   - No Windows:
     ```sh
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
3. Instale as dependências necessárias:
   ```sh
   pip install pandas fastapi uvicorn
   ```
4. Execute o servidor FastAPI:
   ```sh
   python -m uvicorn main:app --reload
   ```

## Executando a aplicação

- Certifique-se de que o backend FastAPI está rodando.
- No outro terminal, execute o frontend Vue.js:
  ```sh
  npm run serve
  ```
