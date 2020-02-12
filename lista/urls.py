from django.urls import path
from .views import *

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="index"),
    path('cadastrar/produto/', ProdutoCreate.as_view(), name="cadastrar-produto"),
    
]
 
