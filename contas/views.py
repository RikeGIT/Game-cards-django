from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import Perfil

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_staff = False
            user.is_superuser = False
            user.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'contas/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'contas/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    perfil = Perfil.objects.get(user=request.user)
    return render(request, 'contas/home.html', {'perfil': perfil})
