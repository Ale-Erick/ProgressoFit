from django.shortcuts import render

# Create your views here.
def home_view(request): 
    return render(request, "home.html") 

def login_view(request): 
    return render(request, "contas/login.html") 

def cadastro_view(request): 
    return render(request, "contas/cadastro.html") 

def perfil_view(request): 
    return render(request, "contas/perfil.html") 

def perfil_editar_view(request): 
    return render(request, "contas/perfil_editar.html") 

def verificacao_view(request): 
    return render(request, "contas/verificacao.html") 