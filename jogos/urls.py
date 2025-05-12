from django.urls import path
from .views import (
    JogoListView, JogoDetailView, JogoCreateView,
    JogoUpdateView, JogoDeleteView, avaliar_jogo
)

urlpatterns = [
    path('', JogoListView.as_view(), name='home'),
    path('jogo/<int:pk>/', JogoDetailView.as_view(), name='jogo_detalhes'),

    # CRUD
    path('painel/jogos/', JogoCreateView.as_view(), name='jogos_admin'),
    path('painel/jogos/editar/<int:pk>/', JogoUpdateView.as_view(), name='jogo_editar'),
    path('painel/jogos/excluir/<int:pk>/', JogoDeleteView.as_view(), name='jogo_excluir'),

    # Avaliação
    path('avaliar/<int:jogo_id>/', avaliar_jogo, name='avaliar_jogo'),
]
