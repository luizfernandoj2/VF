from django.db import models

# Create your models here.

class alunos(models.Model):

    nome = models.CharField(max_length=80)
    endereco = models.CharField(max_length=80)
    email = models.CharField(max_length=80)

def __str__(self):
    return self.nome