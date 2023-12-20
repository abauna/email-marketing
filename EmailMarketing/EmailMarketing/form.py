import re
from .models import Email
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



    


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = [
            'email',
            'senha',
            'assunto',
            'destiny',
            'anexo',
        ]