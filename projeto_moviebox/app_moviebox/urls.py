from django.urls import path
from .views import VerTarefa, DetalheTarefa, CriarTarefa, EditarTarefa, DeletarTarefa

urlpatterns = [
    path('', VerTarefa.as_view(), name='home'),
    path('tarefa/<int:pk>', DetalheTarefa.as_view(), name='tarefa'),
    path('criar-tarefa/', CriarTarefa.as_view(), name='criar-tarefa'),
    path('editar-tarefa/<int:pk>', EditarTarefa.as_view(), name='editar-tarefa'),
    path('deletar-tarefa/<int:pk>', DeletarTarefa.as_view(), name='deletar-tarefa'),
]
