from django.shortcuts import render 
def treinos_view(request): 
    return render(request, "planos/treinos.html") 

def nutricao_view(request): 
    return render(request, "planos/nutricao.html") 

def validacoes_view(request): 
    return render(request, "planos/validacoes.html")