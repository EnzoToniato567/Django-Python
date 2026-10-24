from django.contrib import admin

from .django_db import Categoria, Produto

admin.site.register(Categoria)
admin.site.register(Produto)
