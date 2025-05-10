# jogos/views.py
from django.views.generic import ListView, DetailView, View
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from .models import Jogo
from .forms import JogoForm

# VIEWS PUBLICAS

# listar todos os jogos
class JogoListView(ListView):
    model = Jogo
    template_name = 'jogos/pages/home.html' 
    context_object_name = 'jogos' 

# View publica para mostrar os detalhes de um jogo específico
class JogoDetailView(DetailView):
    model = Jogo
    template_name = 'jogos/pages/detalhes.html' 
    context_object_name = 'jogo'  

# VIEWS PRIVADAS

class JogoUnifiedView(View):
    template_name = 'jogos/pages/jogos_crud.html'

    def get(self, request, pk=None):
        if pk:
            jogo = get_object_or_404(Jogo, pk=pk)
            form = JogoForm(instance=jogo)
        else:
            form = JogoForm()
        jogos = Jogo.objects.all()
        return render(request, self.template_name, {'form': form, 'jogos': jogos, 'editando': pk})

    def post(self, request, pk=None):
        if pk:
            jogo = get_object_or_404(Jogo, pk=pk)
            form = JogoForm(request.POST, request.FILES, instance=jogo)
        else:
            form = JogoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('jogos_unificados')

        jogos = Jogo.objects.all()
        return render(request, self.template_name, {'form': form, 'jogos': jogos, 'editando': pk})

@method_decorator(require_POST, name='dispatch')
class JogoDeleteView(View):
    def post(self, request, pk):
        jogo = get_object_or_404(Jogo, pk=pk)
        jogo.delete()
        return redirect('jogos_unificados')