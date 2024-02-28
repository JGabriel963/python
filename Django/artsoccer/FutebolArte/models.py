from django.db import models

DIVISAO_ATUAL = (
    ("A", "Divisão A"),
    ("B", "Divisão B"),
    ("C", "Divisão C"),
    ("D", "Divisão D"),
)

ESTADO_CHOICE = (
    ("PI", "Piauí"),
    ("MA", "Maranhão")
)

GENERO = (
    ("M", "Masculino"),
    ("F", "Femenino")
)

POSITION = (
    "Atacante",
    "Zagueiro",
    "Goleiro",
    "Basico"
)

class Jogador(models.Model):
    nome = models.CharField(max_length="120", null=False)
    posicao = models.CharField(choices=POSITION , max_length=120, default="Basico")

    


# Create your models here.
class Clube(models.Model):
    nome = models.CharField(max_length=120, null=False, blank=False)
    ano_fundacao = models.PositiveBigIntegerField(default=2024)
    divisao_atual = models.CharField(choices=DIVISAO_ATUAL, max_length=10)
    cidade = models.CharField(max_length=120, null=False, blank=False)
    uf = models.CharField(choices=ESTADO_CHOICE, max_length=40)
    genero = models.CharField(choices=GENERO, max_length=80)
    
    def __str__(self) -> str:
        return self.nome