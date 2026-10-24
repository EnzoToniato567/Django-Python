
from django.urls import path

from .controllers.categorias_controller import CategoriaController
from .controllers.produtos_controller import ProdutoController


def rota(controller, acao):
    return controller.as_view(acao)


urlpatterns = [

    path("categorias/listar", rota(CategoriaController, {"get": "list"})),
    path("categorias/cadastrar", rota(CategoriaController, {"post": "create"})),
    path("categorias/buscar/<int:pk>", rota(CategoriaController, {"get": "retrieve"})),
    path("categorias/atualizar/<int:pk>", rota(CategoriaController, {"put": "update", "patch": "partial_update"})),
    path("categorias/excluir/<int:pk>", rota(CategoriaController, {"delete": "destroy"})),

    path("produtos/listar", rota(ProdutoController, {"get": "list"})),
    path("produtos/cadastrar", rota(ProdutoController, {"post": "create"})),
    path("produtos/buscar/<int:pk>", rota(ProdutoController, {"get": "retrieve"})),
    path("produtos/atualizar/<int:pk>", rota(ProdutoController, {"put": "update", "patch": "partial_update"})),
    path("produtos/excluir/<int:pk>", rota(ProdutoController, {"delete": "destroy"})),
]
