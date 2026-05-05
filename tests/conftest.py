import pytest
from fastapi.testclient import TestClient
from main import app  

@pytest.fixture
def client():
    """Retorna uma instância do TestClient para os testes."""
    return TestClient(app)

@pytest.fixture
def prato_valido():
    """Payload de prato válido reutilizável nos testes."""
    return {
        "nome": "Prato de Teste",
        "categoria": "massa",
        "preco": 40.0,
        "disponivel": True
    }
    
    
# Observe que não há mais 'client = TestClient(app)' aqui

def test_raiz_retorna_nome_restaurante(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Bella Tavola" in response.json()["restaurante"]

def test_listar_pratos_retorna_200(client):
    response = client.get("/pratos")
    assert response.status_code == 200

def test_listar_pratos_retorna_lista(client):
    response = client.get("/pratos")
    assert isinstance(response.json(), list)

def test_listar_pratos_retorna_pelo_menos_um_prato(client):
    response = client.get("/pratos")
    assert len(response.json()) > 0

def test_buscar_prato_inexistente_retorna_404(client):
    response = client.get("/pratos/9999")
    assert response.status_code == 404

# Exemplo de como usar a outra fixture 'prato_valido' se necessário:
def test_exemplo_com_payload(client, prato_valido):
    # Aqui você usa o 'prato_valido' injetado pelo conftest
    assert prato_valido["categoria"] == "massa"