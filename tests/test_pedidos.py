from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

# função pratos se existir na API

def test_raiz_retorna_nome_restaurante():
    response = client.get("/")
    assert response.status_code == 200
    assert "Bella Tavola" in response.json()["restaurante"]

def test_listar_pratos_retorna_200():
    response = client.get("/pratos")
    assert response.status_code == 200

def test_listar_pratos_retorna_lista():
    response = client.get("/pratos")
    assert isinstance(response.json(), list)

def test_listar_pratos_retorna_pelo_menos_um_prato():
    response = client.get("/pratos")
    assert len(response.json()) > 0

def test_buscar_prato_inexistente_retorna_404():
    response = client.get("/pratos/9999")
    assert response.status_code == 404

# Adicionando bebidas 

def test_listar_bebidas_retorna_200():
    response = client.get("/bebidas")
    assert response.status_code == 200

def test_listar_bebidas_retorna_lista():
    response = client.get("/bebidas")
    assert isinstance(response.json(), list)

def test_listar_bebidas_retorna_pelo_menos_uma_bebida():
    response = client.get("/bebidas")
    assert len(response.json()) > 0

def test_buscar_bebida_inexistente_retorna_404():
    response = client.get("/bebidas/9999")
    assert response.status_code == 404