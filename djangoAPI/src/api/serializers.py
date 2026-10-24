from rest_framework import serializers

from ..django_db import Categoria, Produto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']


class ProdutoSerializer(serializers.ModelSerializer):
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(),
        source='categoria',
    )

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'categoria_id']
