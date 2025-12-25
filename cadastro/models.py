from django.db import models

class CadastroPlantas(models.Model):
    nome = models.CharField(max_length=255)
    nomeCientifico = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    regiao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome