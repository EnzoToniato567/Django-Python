from rest_framework.viewsets import ModelViewSet

from ...django_db import Produto
from ..serializers import ProdutoSerializer


class ProdutoController(ModelViewSet):
    queryset = Produto.objects.select_related('categoria').all()
    serializer_class = ProdutoSerializer
