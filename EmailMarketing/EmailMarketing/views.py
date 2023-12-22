from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import Http404

from .form import emailForm
from .processamento import enviar
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html')

def email(request):
    if request.method == 'POST':
        form = emailForm(request.POST, request.FILES)
        if form.is_valid():
            # Processamento dos dados do formulário aqui
            email = form.cleaned_data['email']
            
            assunto = form.cleaned_data['assunto']
            destinos = form.cleaned_data['destino'].split(',')  # Separa os e-mails por vírgula
            destinos = [d.strip() for d in destinos]
            anexo = form.cleaned_data['anexo'] if 'anexo' in request.FILES else None
            concordo = form.cleaned_data['concordo']
            mensagem = enviar(email, assunto, destinos, anexo, concordo)
            # Faça algo com os dados (salvar no banco de dados, enviar e-mail, etc.)
            
    else:
        form = emailForm()
    
    return render(request, 'email.html', {'form': form})

def sobre(request):
    return render(request, 'sobre.html')
def contato(request):
    return render(request, 'contato.html')

