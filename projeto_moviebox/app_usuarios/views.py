from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth import login  

class Logar(LoginView):
    template_name = './login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
class Cadastro(FormView):
    template_name = './cadastro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Cadastro, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(Cadastro, self).get(*args, **kwargs)