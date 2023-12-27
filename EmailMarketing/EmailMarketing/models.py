from django.db import models

class Reposicao(models.Model):
    nome_aluno = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    dia_da_falta = models.DateField()
    dia = models.DateField()
    hora = models.TimeField()
    conteudo = models.CharField(max_length=255)
    concordo = models.BooleanField()

    def __str__(self):
        return self.nome_aluno  # Retorna o nome do aluno ao imprimir um objeto Reposicao
