from django.db import models

DIVISAO = (
    ('A', 'Série A'),
    ('B', 'Série B'),
    ('C', 'Série C'),
    ('D', 'Série D'),
    ('S', 'Sem Série')
)

MODALIDADE = (
  ('M', 'Masculino'),
  ('F', 'Feminino')
)

SEXO = (
    ("M", 'Masculino'),
    ('F', 'Femenino'),
    ('N', "Não informar")
)

class Clube(models.Model):
    nome = models.CharField(max_length=128, blank=False, null=False)
    ano_fundacao = models.PositiveIntegerField("Ano Fundação", help_text="ano que o clube foi criado")
    divisao = models.CharField("Divisão", max_length=60, choices=DIVISAO, default='S', blank=False, null=True)
    modalidade = models.CharField(choices=MODALIDADE, max_length=10, default="M")

    class Meta:
        verbose_name = 'Clube'
        verbose_name_plural = 'Clubes'
    
    def __str__(self) -> str:
        return self.nome


class Jogador(models.Model):
    nome = models.CharField(max_length=128, blank=False, null=False)
    camisa = models.PositiveIntegerField("Nº da camisa")
    sexo = models.CharField(choices=SEXO, max_length=128, default="N")

    clube = models.ForeignKey(Clube, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Jogadores'

    def __str__(self) -> str:
        return self.nome