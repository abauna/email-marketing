from django.db import models



def disponibilidade_padrao():
    return {
        'Segunda': [1] * 24,
        'Terca': [1] * 24,
        'Quarta': [1] * 24,
        'Quinta': [1] * 24,
        'Sexta': [1] * 24,
        'Sabado': [1] * 24,
        'Domingo': [1] * 24
    }

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    disponibilidade = models.JSONField(default=disponibilidade_padrao)

    def __str__(self):
        return self.nome
    
    
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
