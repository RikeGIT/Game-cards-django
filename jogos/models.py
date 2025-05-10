from django.db import models

class Jogo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    estudio = models.CharField(max_length=100)
    data_lancamento = models.DateField()

    capa = models.ImageField(upload_to='capas/')
    background = models.ImageField(upload_to='backgrounds/')

    def __str__(self):
        return self.titulo

