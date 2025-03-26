Configuração do Ambiente

Passo 1: Instalar o Python

Antes de começar, certifique-se de que o Python está instalado no seu sistema. Você pode baixar a versão mais recente no site oficial:

Download Python

Após a instalação, verifique se o Python está corretamente instalado executando o seguinte comando no terminal:

python --version

Passo 2: Criar um Ambiente Virtual

Para isolar as dependências do projeto, crie um ambiente virtual executando o seguinte comando no terminal:

python -m venv venv

Passo 3: Ativar o Ambiente Virtual

Após criar o ambiente virtual, ative-o com o seguinte comando:

venv\Scripts\Activate.ps1

Se estiver utilizando o CMD ao invés do PowerShell, use:

venv\Scripts\activate.bat

Para usuários de Linux ou Mac, utilize:

source venv/bin/activate

Passo 4: Instalar Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias executando:

pip install -r requirements.txt

Passo 5: Executar as Tarefas

Agora, basta rodar os arquivos de tarefa do projeto:

python task1.py
python task2.py

Pronto! Agora o ambiente está configurado e o projeto pode ser executado sem problemas.

