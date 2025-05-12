from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Avg
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from .models import Jogo, Avaliacao
from .forms import JogoForm

# VIEWS PÚBLICAS

class JogoListView(ListView):
    model = Jogo
    template_name = 'jogos/pages/home.html'
    context_object_name = 'jogos'


class JogoDetailView(DetailView):
    model = Jogo
    template_name = 'jogos/pages/detalhes.html'
    context_object_name = 'jogo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jogo = self.object
        media_estrelas = Avaliacao.objects.filter(jogo=jogo).aggregate(Avg("estrelas"))['estrelas__avg'] or 0
        context['media_estrelas'] = round(media_estrelas, 1)
        return context


@login_required
def avaliar_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, id=jogo_id)

    if request.method == "POST":
        estrelas = request.POST.get("estrelas")
        if not estrelas:
            return JsonResponse({"success": False, "error": "Valor de estrelas não recebido."})

        try:
            estrelas = int(estrelas)
            Avaliacao.objects.update_or_create(
                usuario=request.user, jogo=jogo,
                defaults={"estrelas": estrelas}
            )
            media_estrelas = Avaliacao.objects.filter(jogo=jogo).aggregate(Avg("estrelas"))['estrelas__avg'] or 0
            return JsonResponse({"success": True, "media_estrelas": round(media_estrelas, 1)})
        except ValueError:
            return JsonResponse({"success": False, "error": "Erro ao processar avaliação."})

    return JsonResponse({"success": False, "error": "Método inválido."})

# VIEWS PRIVADAS (CRUD ADMIN)

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class JogoCreateView(StaffRequiredMixin, CreateView):
    model = Jogo
    form_class = JogoForm
    template_name = 'jogos/pages/jogos_crud.html'
    login_url = '/login/'
    success_url = reverse_lazy('jogos_admin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jogos'] = Jogo.objects.all()
        return context


class JogoUpdateView(StaffRequiredMixin, UpdateView):
    model = Jogo
    form_class = JogoForm
    template_name = 'jogos/pages/jogos_crud.html'
    success_url = reverse_lazy('jogos_admin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jogos'] = Jogo.objects.all()
        context['editando'] = self.object.pk
        return context


@method_decorator(require_POST, name='dispatch')
class JogoDeleteView(StaffRequiredMixin, DeleteView):
    model = Jogo
    success_url = reverse_lazy('jogos_admin')
