from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Perfil, Cargo

@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        cargo_padrao, _ = Cargo.objects.get_or_create(nome="Usuário")
        Perfil.objects.create(user=instance, cargo=cargo_padrao)
