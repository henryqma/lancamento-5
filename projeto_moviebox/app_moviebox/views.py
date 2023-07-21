from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarefa
from django.contrib.auth.mixins import LoginRequiredMixin



class VerTarefa(LoginRequiredMixin, ListView):
    model = Tarefa
    context_object_name = 'tarefas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarefas'] = context['tarefas'].filter(user=self.request.user)
        context['contar'] = context['tarefas'].filter(status=False).count()
        
        buscar = self.request.GET.get('campo-busca') or ''
        if buscar:
            context['tarefas'] = context['tarefas'].filter(titulo__startswith=buscar)
        
        context['buscar'] = buscar
            
        return context

class DetalheTarefa(LoginRequiredMixin, DetailView):
    model = Tarefa
    context_object_name = 'tarefad'

class CriarTarefa(LoginRequiredMixin, CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'status']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CriarTarefa, self).form_valid(form)

class EditarTarefa(LoginRequiredMixin, UpdateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'status']
    success_url = reverse_lazy('home')

class DeletarTarefa(LoginRequiredMixin, DeleteView):
    model = Tarefa
    context_object_name = 'tarefad'
    success_url = reverse_lazy('home')