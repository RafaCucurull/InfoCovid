from django.forms import ModelForm

from infcovid.models import Consulta


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['consulta', 'categoria',]