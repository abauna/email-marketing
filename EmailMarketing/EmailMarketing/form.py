from django import forms
from .models import Professor
from django.db import models


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'curso', 'disponibilidade']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['disponibilidade'].widget.attrs['rows'] = 7 

    def clean(self):
        cleaned_data = super().clean()
        disponibilidade = cleaned_data.get('disponibilidade')
        
        # Verifica se a disponibilidade está preenchida
        if not disponibilidade:
            self.add_error('disponibilidade', 'Este campo é obrigatório.')
        
        return cleaned_data
class ReposicaoForm(forms.Form):
    nome_aluno = forms.CharField(label='Nome do Aluno', required=True)
    curso = forms.CharField(label='Curso', required=True)
    professor = forms.CharField(label='Professor', required=True)
    dia_da_falta = forms.DateField(label='Data da Falta', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    dia = forms.DateField(label='Data da Reposição', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(label='Hora da Reposição', required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    conteudo = forms.CharField(label='Conteúdo', required=True)
    concordo = forms.BooleanField(label='Concordo com os termos de uso', required=True)
class FiltroReposicaoForm(forms.Form):
    curso = forms.CharField(required=False)
    professor = forms.CharField(required=False)
    dia = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))