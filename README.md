"# Restaurant-API" 
🍽️ Restaurant API
A Restaurant API é uma API REST desenvolvida em Python com FastAPI, criada para demonstrar de forma clara e prática o conceito de API e comunicação entre sistemas.
Este projeto permite cadastrar pratos e listar o cardápio, servindo como um exemplo didático para estudos, apresentações e portfólio.

📖 About the Project
An API (Application Programming Interface) is a way for different systems to communicate with each other.
In this project:

The API represents the restaurant system
The client can be a web app, mobile app, Postman, or Swagger UI
The client sends requests
The API processes the request and returns responses


🧠 Real-world Analogy

Customer requests the menu
Waiter takes the order
Kitchen prepares the food
Food is delivered

👉 The API works like the kitchen: it receives requests and returns results.

🚀 Technologies Used

Python 3
FastAPI
Uvicorn
Pydantic


📁 Project Structure
restaurant_api/
│
├── main.py
├── requirements.txt
└── README.md


⚙️ Installation and Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/restaurant-api.git
cd restaurant-api


2️⃣ Create a virtual environment (recommended)
Shellpython -m venv venvsource venv/bin/activate  # Linux/Macvenv\Scripts\activate     # Windows

3️⃣ Install dependencies
Shellpip install -r requirements.txt

▶️ Running the API
Start the development server with:
Shelluvicorn main:app --reload
The API will be available at:
http://127.0.0.1:8000


📘 Interactive API Documentation
FastAPI automatically generates interactive documentation.
Access:
http://127.0.0.1:8000/docs

With this interface you can:

View all available endpoints
Test requests directly in the browser
Send and receive data without using Postman


📌 Available Endpoints
✅ List all dishes
GET /pratos
Returns a list of all registered dishes.

✅ Create a new dish
POST /pratos
Request body example:
JSON{  "nome": "Pizza Margherita",  "preco": 35.90,  "disponivel": true}
Response:
JSON{  "mensagem": "Prato cadastrado com sucesso"}

🧪 How to Test the API
You can test this API using:

Swagger UI (/docs)
Postman
Python scripts
Any front-end application


🔍 API vs Client

API: The FastAPI backend (main.py)
Client: Any system that sends requests (Swagger, Postman, app, website)

👉 The client requests
👉 The API responds

🎯 Project Purpose
This project was created to:

Learn and demonstrate API concepts
Practice RESTful endpoints
Serve as a portfolio and study reference


📄 License
This project is for educational purposes.

🍽️ API de Restaurante
A API de Restaurante é uma API REST desenvolvida em Python com FastAPI, criada para demonstrar de forma simples e prática o que é uma API e como funciona a comunicação entre sistemas.
Este projeto permite cadastrar pratos e listar o cardápio, sendo ideal para estudos, apresentações e portfólio.

📖 Sobre o Projeto
Uma API (Application Programming Interface) é um meio de comunicação entre sistemas.
Neste projeto:

A API representa o sistema do restaurante
O cliente pode ser um site, aplicativo, Postman ou Swagger
O cliente envia uma requisição
A API processa a requisição e retorna uma resposta


🧠 Analogia com o mundo real

O cliente pede o cardápio
O garçom leva o pedido
A cozinha prepara
O prato é entregue

👉 A API funciona como a cozinha: recebe pedidos e devolve resultados.

🚀 Tecnologias Utilizadas

Python 3
FastAPI
Uvicorn
Pydantic


📁 Estrutura do Projeto
api_restaurante/
│
├── main.py
├── requirements.txt
└── README.md


⚙️ Instalação e Configuração
1️⃣ Clone o repositório
Shellgit clone https://github.com/seu-usuario/api-restaurante.gitcd api-restaurante

2️⃣ Crie um ambiente virtual (recomendado)
Shellpython -m venv venv
Ative o ambiente:

Windows

Shellvenv\Scripts\activate

Linux / Mac

Shellsource venv/bin/activate

3️⃣ Instale as dependências
Shellpip install -r requirements.txt

▶️ Executando a API
Inicie o servidor com o comando:
Shelluvicorn main:app --reload
A API ficará disponível em:
http://127.0.0.1:8000


📘 Documentação Interativa (Swagger)
O FastAPI gera automaticamente uma documentação interativa.
👉 Acesse:
http://127.0.0.1:8000/docs

Nesta interface é possível:

Visualizar todas as rotas da API
Testar os endpoints diretamente no navegador
Enviar e receber dados sem usar Postman


📌 Endpoints Disponíveis
✅ Listar pratos
GET /pratos
Retorna todos os pratos cadastrados.

✅ Cadastrar prato
POST /pratos
Exemplo de corpo da requisição:
JSON{  "nome": "Pizza Margherita",  "preco": 35.90,  "disponivel": true}
Resposta:
JSON{  "mensagem": "Prato cadastrado com sucesso"}

🧪 Como Testar a API
A API pode ser testada utilizando:

Swagger (/docs)
Postman
Código em Python
Aplicações web ou mobile


🔍 Quem é o Cliente e quem é a API?

API: código backend desenvolvido com FastAPI (main.py)
Cliente: qualquer sistema que faz requisições (Swagger, Postman, app, site)

👉 O cliente solicita
👉 A API responde

🎯 Objetivo do Projeto
Este projeto foi criado com o objetivo de:

Aprender e explicar o conceito de APIs
Praticar endpoints REST
Demonstrar comunicação entre sistemas
Servir como projeto de estudo e portfólio


📄 Licença
Este projeto é destinado para fins educacionais.

## O que é necessário para criar uma API?

Para criar uma API em qualquer linguagem de programação, é necessário:

- Uma linguagem de programação
- Um framework ou biblioteca web
- Definição de rotas (endpoints)
- Uso de métodos HTTP (GET, POST, PUT, DELETE)
- Um formato padrão de dados, como JSON
- Um servidor para disponibilizar a API