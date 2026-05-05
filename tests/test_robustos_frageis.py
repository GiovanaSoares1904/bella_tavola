import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestPratos:
    
    def test_listar_pratos_sucesso(self):
        response = client.get("/pratos")
        
        assert response.status_code == 200
        dados = response.json()
        
        # Agora verificamos se o retorno principal é uma lista
        assert isinstance(dados, list)

    def test_conteudo_lista_pratos(self):
        response = client.get("/pratos")
        dados = response.json()
        
        if len(dados) > 0:
            # Pegamos o primeiro item da lista
            primeiro_prato = dados[0]
            # Verificamos os campos que apareceram no seu log de erro
            assert "nome" in primeiro_prato
            assert "categoria" in primeiro_prato
            assert "disponivel" in primeiro_prato
        else:
            pytest.skip("A lista de pratos está vazia, não foi possível validar os campos internos.")

    def test_buscar_prato_inexistente(self):
        id_invalido = 9999
        response = client.get(f"/pratos/{id_invalido}")
        
        assert response.status_code == 404