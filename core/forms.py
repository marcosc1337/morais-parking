from django.forms import ModelForm
from core.models import Veiculo


class CadastroVeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'proprietario', 'matricula', 'curso', 'area_especial']
