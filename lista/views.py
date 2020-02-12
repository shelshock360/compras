from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.urls import reverse_lazy 

# importaçao pra alterar excluir consultar
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class PaginaInicialView(TemplateView):
    template_name = "lista/index.html"


class ProdutoCreate (CreateView):
    model = Produto
    fields = ['nome','preco','qtde']
    template_name = 'lista/formulario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoCreate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Cadastro de novos produtos"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context
    




