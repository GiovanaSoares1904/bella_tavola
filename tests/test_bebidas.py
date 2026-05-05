from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

# função de bebidas na API, verificando a chave 'bebidas' existe e retorna uma lista 

def test_listar_bebidas_retorna_200():
    response = client.get("/bebidas")
    assert response.status_code == 200

# def test_listar_bebidas_retorna_lista():
#     response = client.get("/bebidas")
#     dados = response.json()
#     assert "bebidas" in dados
#     assert isinstance(dados["bebidas"], list)

def test_listar_bebidas_retorna_pelo_menos_uma_bebida():
    response = client.get("/bebidas")
    dados = response.json()
    assert len(dados["bebidas"]) > 0

def test_buscar_bebida_inexistente_retorna_404():
    response = client.get("/bebidas/9999")
    assert response.status_code == 404