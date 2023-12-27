from django.shortcuts import render, redirect
from .models import Reposicao
from .form import ReposicaoForm,FiltroReposicaoForm # Importando o novo formulário
def teste(request):
    reposicoes = Reposicao.objects.all()  # Pega todas as instâncias do modelo Reposicao
    return render(request, 'teste.html', {'reposicoes': reposicoes})
def enviar_email(request):
    if request.method == 'POST':
        form = ReposicaoForm(request.POST)
        if form.is_valid():
            # Aqui você pode processar os dados do formulário
            dados_formulario = form.cleaned_data
            reposicao = Reposicao(
                nome_aluno=dados_formulario['nome_aluno'],
                curso=dados_formulario['curso'],
                professor=dados_formulario['professor'],
                dia_da_falta=dados_formulario['dia_da_falta'],
                dia=dados_formulario['dia'],
                hora=dados_formulario['hora'],
                conteudo=dados_formulario['conteudo'],
                concordo=dados_formulario['concordo']
            )
            # Salve a instância no banco de dados
            reposicao.save()

            
            print("Formulário válido. Redirecionando para a página de sucesso.")
            return render(request, 'sucesso.html', {'dados_formulario': form.cleaned_data})
        else:
            print("Formulário inválido. Erros:")
            print(form.errors)  # Imprime os erros do formulário no console
            print("Valores submetidos:")
            print(request.POST)
    else:
        form = ReposicaoForm()
    
    return render(request, 'home.html', {'form': form})
def sucesso(request):
    # Você pode processar os dados aqui se necessário antes de exibi-los na página de sucesso
    dados_formulario = request.POST  # Supondo que os dados foram passados via POST

    return render(request, 'sucesso.html', {'dados_formulario': dados_formulario})
def listar_reposicoes(request):
    reposicoes = Reposicao.objects.all()
    filtro_form = FiltroReposicaoForm(request.GET)

    if filtro_form.is_valid():
        curso = filtro_form.cleaned_data.get('curso')
        professor = filtro_form.cleaned_data.get('professor')

        if curso:
            reposicoes = reposicoes.filter(curso=curso)
        if professor:
            reposicoes = reposicoes.filter(professor=professor)

    return render(request, 'lista_reposicoes.html', {'reposicoes': reposicoes, 'filtro_form': filtro_form})