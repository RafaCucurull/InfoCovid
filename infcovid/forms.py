from django.forms import ModelForm, Textarea
from infcovid.models import Consulta


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['consulta', 'categoria', ]
        widgets = {'consulta': Textarea(attrs={'cols': 145, 'rows': 10})}
