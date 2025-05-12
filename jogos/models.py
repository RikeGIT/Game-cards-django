from django.db import models
from django.contrib.auth.models import User

class Jogo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    estudio = models.CharField(max_length=100)
    data_lancamento = models.DateField()
    capa = models.ImageField(upload_to='capas/')
    background = models.ImageField(upload_to='backgrounds/')

    def __str__(self):
        return self.titulo

    def media_avaliacao(self):
        return Avaliacao.objects.filter(jogo=self).aggregate(Avg("estrelas"))["estrelas__avg"] or 0


class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário que avaliou
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)  # Jogo avaliado
    estrelas = models.PositiveIntegerField(choices=[(i, f"{i} Estrela(s)") for i in range(1, 6)])  # De 1 a 5 estrelas
    data_avaliacao = models.DateTimeField(auto_now_add=True)
