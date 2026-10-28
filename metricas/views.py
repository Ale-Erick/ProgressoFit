from django.shortcuts import render, get_object_or_404
from . import models


def registrar_view(request):
    return render(request, "metricas/registrar.html")

def evolucao_view(request):
    metricas = models.MetricaCorporal.objects.all()
    return render(request, "metricas/lista.html", {"metricas": metricas})

def detalhe_view(request, metrica_id):
    metrica = get_object_or_404(models.MetricaCorporal, id=metrica_id)
    return render(request, "metricas/detalhe.html", {"metrica": metrica})