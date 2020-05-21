from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.forms import  CadastroVeiculoForm
from core.models import Veiculo


@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def cadastrarVeiculo(request):
    if request.method == 'POST':
        form = CadastroVeiculoForm(request.POST)
    else: 
        form = CadastroVeiculoForm()
        
    if form.is_valid():
        form.save()
        return redirect('index')
    formContextToRender = {'form': form}
    return render(request, 'cadastrar-veiculo.html',formContextToRender )
