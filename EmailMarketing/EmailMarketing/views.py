from django.shortcuts import render
from .form import EmailForm
from django.http import JsonResponse

def get_professores(request):
    curso_selecionado = request.GET.get('curso')

    if curso_selecionado == 'curso1':
        professores = [
            {'id': 'andre', 'nome': 'Andre'},
            {'id': 'natalia', 'nome': 'Natalia'}
        ]
    elif curso_selecionado == 'curso2':
        professores = [
            {'id': 'leandro', 'nome': 'Leandro'},
            {'id': 'vanderlei', 'nome': 'Vanderlei'},
            {'id': 'jackson', 'nome': 'Jackson'}
        ]
    else:
        professores = []

    return JsonResponse(professores, safe=False)
def gerencia(request):
    return render(request, 'formulario.html', {'form': form})
def enviar_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            # Aqui você pode processar os dados do formulário
            nome_aluno = form.cleaned_data['curso']
            curso = form.cleaned_data['curso']
            professor = form.cleaned_data['professor']
            dia_da_falta=form.cleaned_data['dia_da_falta']
            dia = form.cleaned_data['dia']
            hora = form.cleaned_data['hora']
            conteudo = form.cleaned_data['conteudo']
            concordo = form.cleaned_data['concordo']
            anexo = request.FILES.get('anexo') if 'anexo' in request.FILES else None

            # Coloque aqui a lógica para enviar o e-mail com os dados coletados

            # Após enviar o e-mail, você pode redirecionar para uma página de sucesso
            return render(request, 'sucesso.html')
    else:
        form = EmailForm()
    
    return render(request, 'home.html', {'form': form})
