# @title
import pytest


@pytest.mark.parametrize("categoria_invalida", [
    "esoterico",
    "fastfood",
    "japonesa",
    "PIZZA",        # case-sensitive — não é igual a 'pizza'
    "massa extra",  # espaço não permitido pelo pattern
])
def test_categoria_invalida_retorna_422(client, categoria_invalida):
    prato = {
        "nome": "Prato Teste",
        "categoria": categoria_invalida,
        "preco": 40.0
    }
    response = client.post("/pratos", json=prato)
    assert response.status_code == 422


# IDs sintaticamente válidos mas inexistentes → espera 404
@pytest.mark.parametrize("id_inexistente", [9999, 123456, 99999])
def test_prato_inexistente_retorna_404(client, id_inexistente):
    response = client.get(f"/pratos/{id_inexistente}")
    assert response.status_code == 404


@pytest.mark.parametrize("categoria_valida", [
    "pizza",
    "massa",
    "sobremesa",
    "entrada",
    "salada",
])
def test_filtro_por_categoria_valida(client, categoria_valida):
    response = client.get(f"/pratos?categoria={categoria_valida}")
    assert response.status_code == 200
    pratos = response.json()
    for prato in pratos:
        assert prato["categoria"] == categoria_valida