from django.shortcuts import render, redirect, get_object_or_404
from core.forms import  CadastroVeiculoForm
from core.models import Veiculo

def home(request):
    return render(request, 'index.html')

def cadastrarVeiculo(request):
    form = CadastroVeiculoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    formContextToRender = {'form': form}
    return render(request, 'cadastrar-veiculo.html',formContextToRender )
