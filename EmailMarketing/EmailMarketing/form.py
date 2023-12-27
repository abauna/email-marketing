from django import forms

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