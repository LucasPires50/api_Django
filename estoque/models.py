from django.db import models

class EstoqueInterno(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.CharField(max_length=5)

    def __str__(self):
        return self.nome

    