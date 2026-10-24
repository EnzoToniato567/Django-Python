from django.test import TestCase
from rest_framework.test import APIClient


class CatalogoTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    # crud categorias

    def test_listar_categorias(self):
        resposta = self.client.get("/categorias/listar")
        self.assertEqual(resposta.status_code, 200)

    def test_cadastrar_categoria(self):
        resposta = self.client.post(
            "/categorias/cadastrar",
            {},
            format="json",
        )
        self.assertIn(resposta.status_code, [201, 400])

    def test_buscar_categoria(self):
        # id fixo usado na URL para buscar a categoria de ID 1 no banco de teste
        id = 1
        resposta = self.client.get(f"/categorias/buscar/{id}")
        self.assertIn(resposta.status_code, [200, 404])

    def test_atualizar_categoria(self):
        id = 1
        resposta = self.client.patch(
            f"/categorias/atualizar/{id}",
            {},
            format="json",
        )
        self.assertIn(resposta.status_code, [200, 400, 404])

    def test_excluir_categoria(self):
        id = 1
        resposta = self.client.delete(f"/categorias/excluir/{id}")
        self.assertIn(resposta.status_code, [204, 400, 404])

    # crud produtos

    def test_listar_produtos(self):
        resposta = self.client.get("/produtos/listar")
        self.assertEqual(resposta.status_code, 200)

    def test_cadastrar_produto(self):
        resposta = self.client.post(
            "/produtos/cadastrar",
            {},
            format="json",
        )
        self.assertIn(resposta.status_code, [201, 400])

    def test_buscar_produto(self):
        id = 1
        resposta = self.client.get(f"/produtos/buscar/{id}")
        self.assertIn(resposta.status_code, [200, 404])

    def test_atualizar_produto(self):
        id = 1
        resposta = self.client.patch(
            f"/produtos/atualizar/{id}",
            {},
            format="json",
        )
        self.assertIn(resposta.status_code, [200, 400, 404])

    def test_excluir_produto(self):
        id = 1
        resposta = self.client.delete(f"/produtos/excluir/{id}")
        self.assertIn(resposta.status_code, [204, 404])
