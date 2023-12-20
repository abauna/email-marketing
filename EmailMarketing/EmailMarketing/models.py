from django.contrib.auth.models import User
from django.db import models
class Email(models.Model):
    email = models.EmailField(max_length=65)
    senha = models.CharField(max_length=65)
    assunto = models.CharField(max_length=65)
    destiny = models.CharField(max_length=165)
    anexo = models.FileField()
    