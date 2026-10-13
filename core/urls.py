from django.urls import path
from . import views

urlpatterns = [
    path('', views.projeto_list, name='projeto_list'),
    path('projetos/novo/', views.projeto_create, name='projeto_create'),
    path('tarefas/', views_tarefas.tarefa_list, name='tarefa_list'),
    path('tarefas/nova/', views_tarefas.tarefa_create, name='tarefa_create'),
    path('tarefas/<int:pk>/editar/', views_tarefas.tarefa_update, name='tarefa_update'),
    path('tarefas/<int:pk>/excluir/', views_tarefas.tarefa_delete, name='tarefa_delete'),
]