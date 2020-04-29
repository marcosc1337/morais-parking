from django.urls import path
from core.views import home, cadastrarVeiculo

urlpatterns = [
    path('', home, name="index"),
    path('cadastrar-veiculo/', cadastrarVeiculo, name='cadastrar-veiculo')
]
