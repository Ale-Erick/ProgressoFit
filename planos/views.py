from django.shortcuts import render
from . import models


def treinos_view(request):
    treinos = models.Treino.objects.all()
    return render(request, "planos/treinos.html", {"treinos": treinos})

def nutricao_view(request):
    planos = models.PlanoAlimentar.objects.all()
    return render(request, "planos/nutricao.html", {"planos": planos})

def validacoes_view(request):
    planos = models.PlanoAlimentar.objects.all()
    return render(request, "planos/validacoes.html", {"planos": planos})