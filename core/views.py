from django.shortcuts import render, redirect
from .models import Projeto
from .forms import ProjetoForm

def projeto_list(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/projeto_list.html', {'projetos': projetos})

def projeto_create(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('projeto_list')
    return render(request, 'core/projeto_form.html', {'form': form})