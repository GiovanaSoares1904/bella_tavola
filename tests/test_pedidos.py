from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

# def test_listar_pedidos_retorna_200():
#     response = client.get("/pedidos")
#     assert response.status_code == 200

# def test_listar_pedidos_retorna_lista():
#     response = client.get("/pedidos")
#     dados = response.json()
    
#     assert "pedidos" in dados
#     assert isinstance(dados["pedidos"], list)

# def test_listar_pedidos_retorna_pelo_menos_um_pedido():
#     response = client.get("/pedidos")
#     dados = response.json()
#     assert len(dados["pedidos"]) > 0

# def test_buscar_pedido_inexistente_retorna_404():
#     response = client.get("/pedidos/9999")
#     assert response.status_code == 404