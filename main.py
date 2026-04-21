from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API Restaurante")

# "Banco de Dados " simples(em memória)
pratos = []

#Modelo prato
class Prato(BaseModel):
    nome: str
    preco: float
    disponivel: bool =True
    
#Listar pratos(GET)
@app.get("/pratos")
def listar_pratos():
    return pratos

#Adicionar prato(POST)
@app.post("/pratos")
def criar_prato(prato: Prato):
    pratos.append(prato)
    return {"mensagem": "Prato cadastro com sucesso "}
    