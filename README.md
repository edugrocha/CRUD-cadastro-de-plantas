# CRUD Django – Cadastro de Plantas

Projeto desenvolvido em **Django** com o objetivo de praticar a criação de um **CRUD (Create, Read, Update, Delete)**. A aplicação permite o cadastro e gerenciamento de informações sobre plantas, utilizando **Bootstrap** para a estilização da interface.

## Funcionalidades
- Cadastrar plantas  
- Listar plantas cadastradas  
- Atualizar informações  
- Excluir registros  

## Campos do cadastro
- Nome  
- Nome científico  
- Descrição  
- Região  

## Tecnologias utilizadas
- Python  
- Django  
- SQLite  
- HTML  
- Bootstrap  
- Git e GitHub  

## Como executar o projeto
1. Clone o repositório:

   ```bash
   git clone https://github.com/edugrocha/CRUD-DJANGO.git
   ```
2. Acesse a pasta do projeto:

   ```bash
   cd CRUD-DJANGO
   ```
3. Crie e ative o ambiente virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
4. Instale o Django:

   ```bash
   pip install django
   ```
5. Execute as migrações:

   ```bash
   python manage.py migrate
   ```
6. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```
7. Acesse no navegador:

   ```
   http://127.0.0.1:8000/
   ```

## Objetivo do projeto

Projeto de estudo para consolidar os conceitos básicos do Django, incluindo criação de CRUD, organização de apps, rotas, models, views e uso do Bootstrap para interfaces responsivas.
