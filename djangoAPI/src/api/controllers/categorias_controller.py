from django.db.models.deletion import ProtectedError
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from ...django_db import Categoria
from ..serializers import CategoriaSerializer


class CategoriaController(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except ProtectedError as error:
            raise ValidationError(
                {'detail': 'Não é possível excluir uma categoria que possui produtos.'}
            ) from error
