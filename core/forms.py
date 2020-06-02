from django.forms import ModelForm
from core.models import Veiculo
from core.models import Entrada


class CadastroVeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'proprietario', 'matricula', 'curso', 'area_especial']

class EntradaVeiculosForm(ModelForm):
    class Meta:
        model = Entrada
        fields = ['setor_type','placa','data_joined']
