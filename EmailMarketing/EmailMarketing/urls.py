"""
URL configuration for EmailMarketing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from . import views

app_name = 'EmailMarketing'

urlpatterns = [
    
  path('admin/', admin.site.urls),
  path('lista_reposicoes/', views.listar_reposicoes, name='lista_reposicoes'),
  path('', views.enviar_email, name='enviar_email'),
  path('home/', views.enviar_email, name='enviar_email'),# Home
  path('sucesso/', views.sucesso, name='sucesso'),
  path('teste/', views.teste, name='teste'),
  path('professores/', views.professores, name='professores'),
     path('professores/<int:pk>/editar/', views.editar_professor, name='editar_professor'),
  path('professores/deletar/<int:pk>/', views.deletar_professor, name='deletar_professor'),
]
