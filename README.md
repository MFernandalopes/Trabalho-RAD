# RAD Control - Sistema de Gestão de Solicitações

## Descrição

O RAD Control é um sistema desenvolvido em Python utilizando Tkinter e PostgreSQL para o gerenciamento de solicitações acadêmicas.

O sistema permite cadastrar, consultar, atualizar, pesquisar e excluir as solicitações, armazenando os dados em um banco de dados PostgreSQL.

## Tecnologias Utilizadas

* Python 3
* Tkinter
* PostgreSQL
* Psycopg2
* Faker

## Funcionalidades

* Cadastro de solicitações
* Listagem de registros
* Pesquisa por nome, status ou prioridade 
* Atualização de registros
* Exclusão de registros com confirmação
* Geração automática de registros fictícios utilizando Faker

## Estrutura do Projeto

* app.py → É a interface gráfica do sistema
* database.py → Operações do banco de dados
* script.sql → Criação da tabela no PostgreSQL
* seed.py → Geração de dados fictícios
* requirements.txt → Dependências do projeto

## Como Executar

### 1. Criar o banco de dados

Executar o arquivo script.sql no PostgreSQL.

### 2. Instalar as dependências


pip install -r requirements.txt
```


python seed.py
```

### 4. Executar o sistema


python app.py
```

## Autor

Maria Fernanda Pires Lopes

Trabalho desenvolvido para a disciplina de Desenvolvimento Rápido de Aplicações (RAD).
