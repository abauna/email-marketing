
    

from django import forms

class emailForm(forms.Form):
    email = forms.EmailField(label='Seu E-mail')
    
    assunto = forms.CharField(label='Assunto', max_length=100)
    destino = forms.CharField(label='E-mails de Destino', help_text='Digite os e-mails separados por vírgula')
    anexo = forms.FileField(label='Anexo', required=False)
    concordo = forms.BooleanField(label='Concordo com os termos de uso', required=True)