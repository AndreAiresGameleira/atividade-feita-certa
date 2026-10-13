from django.shortcuts import render, redirect
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm

def projeto_list(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/projeto_list.html', {'projetos': projetos})

def projeto_create(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('projeto_list')
    return render(request, 'core/projeto_form.html', {'form': form})


def tarefa_list(request):
    tarefas = Tarefa.objects.select_related('projeto')
    return render(request, 'core/tarefa_list.html', {'tarefas': tarefas})

def tarefa_create(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tarefa criada com sucesso!')
        return redirect('tarefa_list')
    return render(request, 'core/tarefa_form.html', {'form': form})

def tarefa_update(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tarefa atualizada com sucesso!')
        return redirect('tarefa_list')
    return render(request, 'core/tarefa_form.html', {'form': form})

def tarefa_delete(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('tarefa_list')
    return render(request, 'core/tarefa_confirm_delete.html', {'tarefa': tarefa})