from django.shortcuts import render
from core.models import Veiculo

def home(request):
    return render(request, 'index.html')
