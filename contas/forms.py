from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
