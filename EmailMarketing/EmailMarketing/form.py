
from django import forms
PROFESSOR_CHOICES = [
    ('professor1', 'Professor 1'),
    ('professor2', 'Professor 2'),
    ('professor3', 'Professor 3'),
    # Adicione mais professores conforme necessário
]

CURSO_CHOICES = [
    ('curso1', 'Curso 1'),
    ('curso2', 'Curso 2'),
    ('curso3', 'Curso 3'),
    # Adicione mais cursos conforme necessário
]
CONTEUDO_CHOICES = [
    ('curso1 CONTEUDO', 'Curso 1CONTEUDO'),
    ('curso2CONTEUDO', 'Curso 2CONTEUDO'),
    ('curso3CONTEUDO', 'Curso 3CONTEUDO'),
    # Adicione mais cursos conforme necessário
]
class EmailForm(forms.Form):
    nome_aluno = forms.CharField(label='Nome do Aluno', max_length=100)
    curso = forms.ChoiceField(label='Curso', choices=CURSO_CHOICES)
    professor = forms.ChoiceField(label='Professor',  choices=PROFESSOR_CHOICES)
    dia_da_falta = forms.DateField(label='Dia', widget=forms.DateInput(attrs={'type': 'date'}))
    dia = forms.DateField(label='Dia', widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(label='Hora', widget=forms.TimeInput(attrs={'type': 'time'}))
    conteudo = forms.ChoiceField(label='CONTEUDO',  choices=CONTEUDO_CHOICES)
    concordo = forms.BooleanField(label='Concordo com os termos de uso', required=True)
    curso = forms.ChoiceField(label='Curso', choices=(
        ('', 'Selecione o Curso'),
        ('curso1', 'Curso 1'),
        ('curso2', 'Curso 2'),
        # Adicione mais cursos conforme necessário
    ))
    professor = forms.ChoiceField(label='Professor', choices=())
    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['professor'].choices = []

        # Adiciona um atributo de classe para identificar o campo no JavaScript
        self.fields['curso'].widget.attrs['class'] = 'curso-select'

        # Adicione classes ou IDs extras se necessário para identificação no JavaScript
        self.fields['professor'].widget.attrs['class'] = 'professor-select'

        # Adiciona um evento onChange para o campo do curso
        self.fields['curso'].widget.attrs['onchange'] = 'getProfessores()'