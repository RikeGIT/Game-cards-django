from django.db import models
from django.contrib.auth.models import User

class Cargo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.cargo.nome if self.cargo else "Sem cargo"}'