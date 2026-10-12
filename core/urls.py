from django.urls import path
from . import views

urlpatterns = [
    path('', views.projeto_list, name='projeto_list'),
    path('projetos/novo/', views.projeto_create, name='projeto_create'),
]