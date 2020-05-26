from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name="index"),
    path('listar-veiculos/', veiculosList, name="listar-veiculos"),
    path('cadastrar-veiculo/', cadastrarVeiculo, name='cadastrar-veiculo')
]
