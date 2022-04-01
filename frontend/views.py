from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class DetailView(TemplateView):
    template_name = 'detail.html'

class CreateView(TemplateView):
    template_name = 'create.html'
