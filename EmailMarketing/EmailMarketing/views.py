from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import Http404

from .form import RegisterForm
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html')

def email(request):
    
    if request.POST:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'email.html', {
        'form': form,
    })
def email_create(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    return redirect('email')
def sobre(request):
    return render(request, 'sobre.html')
def contato(request):
    return render(request, 'contato.html')

