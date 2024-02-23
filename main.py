from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str,any]] = [
    {
        "id":1,
        "nome":"smartphone",
        "descricao":"desc smartphone",
        "preco":1500.0
     },
     {
        "id":2,
        "nome":"notebook",
        "descricao":"desc notebook",
        "preco":3500.0
     },
     {
        "id":3,
        "nome":"tablet",
        "descricao":"desc tablet",
        "preco":2500.0
     },
]

@app.get("/")
def ola_mundo():
    return {"Ola": "pessoal"}

@app.get("/produtos")
def listar_produtos():
    return produtos

