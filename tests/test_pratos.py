# tests/test_pratos.py
from fastapi.testclient import TestClient 
from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

def test_raiz_retorna_nome_restaurante():
    response = client.get("/")
    assert response.status_code == 200
    assert "Bella Tavola" in response.json()["restaurante"]

def test_listar_pratos_retorna_lista():
    response = client.get("/pratos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_listar_pratos_retorna_pelo_menos_um_prato():
    response = client.get("/pratos")
    assert len(response.json()) > 0