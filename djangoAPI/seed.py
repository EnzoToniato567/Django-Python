import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from decimal import Decimal
from src.django_db import Categoria, Produto


categorias = [
    "Eletrônicos",
    "Roupas",
    "Alimentos",
    "Casa",
    "Esportes"
]

produtos = [
    ("Teclado", "120.00", "Eletrônicos"),
    ("Camiseta", "59.90", "Roupas"),
    ("Café", "18.50", "Alimentos"),
    ("Liquidificador", "149.90", "Casa"),
    ("Bola de futebol", "79.90", "Esportes"),
]

Produto.objects.all().delete()
Categoria.objects.all().delete()

lista_categorias = {
    nome: Categoria.objects.create(nome=nome)
    for nome in categorias
}

for nome, preco, categoria in produtos:
    Produto.objects.create(
        nome=nome,
        preco=Decimal(preco),
        categoria=lista_categorias[categoria]
    )

print("Dados de teste inseridos com sucesso!")