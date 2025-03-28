# Configuração do Ambiente

## Passo 1: Instalar o Python

Antes de começar, certifique-se de que o Python está instalado no seu sistema. Você pode baixar a versão mais recente no site oficial:

[Download Python](https://www.python.org/downloads/)

Após a instalação, verifique se o Python está corretamente instalado executando o seguinte comando no terminal:

```sh
python --version
```

## Passo 2: Criar um Ambiente Virtual

Para isolar as dependências do projeto, crie um ambiente virtual executando o seguinte comando no terminal:

```sh
python -m venv venv
```

## Passo 3: Ativar o Ambiente Virtual

Após criar o ambiente virtual, ative-o com o seguinte comando:

```sh
# No PowerShell (Windows)
venv\Scripts\Activate.ps1
```

```sh
# No CMD (Windows)
venv\Scripts\activate.bat
```

```sh
# No Linux ou Mac
source venv/bin/activate
```

## Passo 4: Instalar Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias executando:

```sh
pip install -r requirements.txt
```

## Passo 5: Executar as Tarefas

Agora, basta rodar os arquivos de tarefa do projeto:

```sh
python task1.py
python task2.py
```

Pronto! Agora o ambiente está configurado e o projeto pode ser executado sem problemas.
