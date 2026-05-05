import pytest

@pytest.mark.smoke
def test_healthcheck(client):
    response = client.get("/health")
    assert response.status_code == 200


@pytest.mark.smoke
def test_listar_pratos(client):
    response = client.get("/pratos")
    assert response.status_code == 200


@pytest.mark.smoke
def test_buscar_prato_por_id(client):
    response = client.get("/pratos/1")
    assert response.status_code == 200