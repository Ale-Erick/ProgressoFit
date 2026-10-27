from django.shortcuts import render 
def registrar_view(request): 
    return render(request, "metricas/registrar.html") 

def evolucao_view(request): 
    return render(request, "metricas/lista.html")
 
def detalhe_view(request, metrica_id): 
    return render(request, "metricas/detalhe.html", {"metrica_id": metrica_id})