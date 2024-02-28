from django.db import models

CONTINENTES = (
    ('ASIA', 'Ásia'),
    ('AMERICA', 'América'),
    ('AFRICA', 'África'),
    ('EUROPA', 'Europa'),
    ('OCEANIA', 'Oceania'),
    ('ANTÁRTIDA', 'Antártida')
)

class Pais(models.Model):
    nome = models.CharField(max_length=120)
    continente = models.CharField(max_length=20, choices=CONTINENTES, null=True)
    

    class Meta:
        verbose_name_plural = 'Países'
    
    def __str__(self) -> str:
        return self.nome
    

class Estado(models.Model):
     nome = models.CharField(max_length=120)
     uf = models.CharField("UF", max_length=20, null=True, blank=False)

     pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=False, blank=False)

     def __str__(self) -> str:
         return self.nome
    
        
class Cidade(models.Model):
    nome = models.CharField(max_length=120)

    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.nome