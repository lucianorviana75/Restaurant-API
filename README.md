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
uvicorn main:app --reload
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
