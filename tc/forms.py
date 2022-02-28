from django.forms import ModelForm

from .models import Automato, Maquina, Sequencia


class AutomatosForm(ModelForm):
    class Meta:
        model = Automato
        fields = '__all__'

class MaquinasForm(ModelForm):
    class Meta:
        model = Maquina
        fields = '__all__'

class SequenciaForm(ModelForm):
    class Meta:
        model = Sequencia
        fields = '__all__'
