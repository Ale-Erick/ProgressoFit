from django.contrib.auth.models import User
from django.db import models
from contas.models import Especialista


class Treino(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="treinos")
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class PlanoAlimentar(models.Model):
    STATUS_CHOICES = (
        ("Pendente", "Pendente"),
        ("Aprovado", "Aprovado"),
        ("Ajustado", "Ajustado"),
        ("Rejeitado", "Rejeitado"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="planos_alimentares")
    especialista = models.ForeignKey(
        Especialista,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="planos_revisados",
    )
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pendente")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.status})"