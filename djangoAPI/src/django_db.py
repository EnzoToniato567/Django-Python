from django.core.validators import MinValueValidator
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'categorias'
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['id']

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='produtos',
        db_column='categoria_id',
    )

    class Meta:
        db_table = 'produtos'
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
        ordering = ['id']

    def __str__(self):
        return self.nome
