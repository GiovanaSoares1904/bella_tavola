from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel
import pytest

app = FastAPI()

# Modelo de dados para documentação e validação
class Prato(BaseModel):
    id: int
    nome: str
    preco: float
    categoria: str

# Simulando um "banco de dados"
pratos = [
    {
        "id": 1,
        "nome": "Calabresa",
        "categoria": "pizza",
        "preco": 45.0,
        "disponivel": True,
    },
    {
        "id": 2,
        "nome": "Fettuccine ao Sugo",
        "categoria": "massa",
        "preco": 52.0,
        "disponivel": True,
    },
    {
        "id": 3,
        "nome": "Nhoque (Ginocchi) ao Molho Branco",
        "categoria": "massa",
        "preco": 58.0,
        "disponivel": False,
    },
    {
        "id": 4,
        "nome": "Cannoli",
        "categoria": "sobremesa",
        "preco": 28.0,
        "disponivel": False,
    },
    {
        "id": 5,
        "nome": "Franco com Catupiry",
        "categoria": "pizza",
        "preco": 49.0,
        "disponivel": True,
    },
    {
        "id": 6,
        "nome": "Palha Italiana",
        "categoria": "sobremesa",
        "preco": 24.0,
        "disponivel": True,
    },
]

@app.get("/")
def read_root():
    return {"restaurante": "Bella Tavola"}

@app.get("/pratos", response_model=List[Prato])
def listar_pratos(categoria: Optional[str] = None):
    # Se houver categoria, filtra; caso contrário, retorna tudo
    if categoria:
        pratos_filtrados = [p for p in pratos if pratos["categoria"] == categoria.lower()]
        return pratos_filtrados
    return pratos

@app.get("/pratos/{prato_id}", response_model=Prato)
def buscar_prato(prato_id: int):
    # Procura o prato pelo ID
    prato = next((p for p in pratos if p["id"] == prato_id), None)
    
    # Se não encontrar, retorna 404
    if prato is None:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
        
    return prato



# Criação de pratos Post

def test_criar_prato_valido():
    novo_prato = {
        "nome": "Funghi Trifolati Teste",   # nome único para evitar colisão
        "categoria": "massa",
        "preco": 54.0,
        "disponivel": True
    }
    response = client.post("/pratos", json=novo_prato)
    assert response.status_code in [200, 201]
    dados = response.json()
    assert dados["nome"] == "Funghi Trifolati Teste"
    assert dados["preco"] == 54.0
    assert "id" in dados


def test_criar_prato_com_preco_negativo_retorna_422():
    prato_invalido = {
        "nome": "Prato Inválido",
        "categoria": "pizza",
        "preco": -10.0
    }
    response = client.post("/pratos", json=prato_invalido)
    assert response.status_code == 422


def test_criar_prato_com_nome_curto_retorna_422():
    prato_invalido = {
        "nome": "AB",   # menos de 3 caracteres
        "categoria": "pizza",
        "preco": 40.0
    }
    response = client.post("/pratos", json=prato_invalido)
    assert response.status_code == 422


def test_criar_prato_com_categoria_invalida_retorna_422():
    prato_invalido = {
        "nome": "Prato Exótico",
        "categoria": "esoterico",
        "preco": 40.0
    }
    response = client.post("/pratos", json=prato_invalido)
    assert response.status_code == 422


def test_prato_criado_aparece_na_listagem():
    # Nome único para não colidir com outros testes ou dados iniciais
    nome_unico = "Tagliatelle Teste XYZ-9871"
    client.post("/pratos", json={
        "nome": nome_unico,
        "categoria": "massa",
        "preco": 68.0
    })
    response = client.get("/pratos")
    nomes = [p["nome"] for p in response.json()]
    assert nome_unico in nomes
