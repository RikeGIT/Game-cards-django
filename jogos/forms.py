from django import forms
from .models import Jogo

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['titulo', 'estudio', 'data_lancamento', 'descricao', 'capa', 'background']
