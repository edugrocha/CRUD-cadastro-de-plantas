# CRUD Django – Cadastro de Plantas

Projeto desenvolvido em **Django** com o objetivo de praticar a criação de um **CRUD (Create, Read, Update, Delete)**. A aplicação permite o cadastro e gerenciamento de informações sobre plantas, utilizando o PostgreSQL como banco de dados robusto, e **Bootstrap** para a estilização da interface.

## Funcionalidades
- Cadastrar plantas  
- Listar plantas cadastradas  
- Atualizar informações  
- Excluir registros  

## Campos do cadastro
- Nome  
- Nome científico  
- Descrição  
- Partes utilizadas
- Usos
- Região  
- Origem

## Tecnologias utilizadas
- Python  
- Django  
- PostgreSQL 
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

   # Linux / Mac
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```
4. Instale as dependências

   ```bash
   pip install -r requirements.txt
   ```
5. Crie o arquivo .env

Na raiz do projeto (mesmo nível do manage.py), crie um arquivo chamado .env:

   ```bash
   DB_NAME=CadastroPlantas
   DB_USER=postgres
   DB_PASSWORD=sua_senha_aqui
   DB_HOST=127.0.0.1
   DB_PORT=5432
   ```

Importante:
O arquivo .env não é versionado;
Nunca suba credenciais diretamente no código;
Cada ambiente (local, produção, servidor) deve possuir seu próprio .env.

6. Execute as migrações:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
7. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```
8. Acesse no navegador:

   ```
   http://127.0.0.1:8000/criar_plantas/
   ```

## Objetivo do projeto

Projeto de estudo para consolidar os conceitos básicos do Django com PostgreSQL. 
Servirá de MVP para o desenvolvimento de um sistema funcional.
O sistema pertencerá ao projeto de extensão Farmácia Viva, no IFPE Jaboatão dos Guararapes, em parceria com o IFPE Vitória de Santo Antão.