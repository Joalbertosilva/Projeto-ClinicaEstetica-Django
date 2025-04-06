# inicio/models.py

from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    imagem_url = models.URLField(max_length=500, blank=True, null=True)
    em_promocao = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
