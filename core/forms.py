from django.forms import ModelForm
from core.models import Veiculo
from core.models import Entrada
from core.models import Evento


class CadastroVeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'proprietario', 'matricula', 'curso', 'area_especial']

class EntradaVeiculosForm(ModelForm):
    class Meta:
        model = Entrada
        fields = ['setor_type','placa']

class EventosForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['evento', 'data', 'descrição']

