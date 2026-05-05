# tests/test_pratos.py
from fastapi.testclient import TestClient 
from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)


def test_listar_pratos_retorna_200():
    response = client.get("/pratos")
    assert response.status_code == 200


def test_listar_pratos_retorna_lista():
    response = client.get("/pratos")
    assert isinstance(response.json(), list)


def test_listar_pratos_retorna_pelo_menos_um_prato():
    response = client.get("/pratos")
    assert len(response.json()) > 0


def test_filtro_por_categoria_retorna_apenas_categoria_correta():
    response = client.get("/pratos?categoria=pizza")
    assert response.status_code == 200
    pratos = response.json()
    for prato in pratos:
        assert prato["categoria"] == "pizza"


def test_buscar_prato_existente_retorna_campos_esperados():
    response = client.get("/pratos/1")
    assert response.status_code == 200
    prato = response.json()
    assert "id" in prato
    assert "nome" in prato
    assert "preco" in prato


def test_buscar_prato_inexistente_retorna_404():
    response = client.get("/pratos/9999")
    assert response.status_code == 404