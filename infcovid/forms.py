from django.forms import ModelForm, Textarea
from infcovid.models import Consulta, Pregunta


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['consulta', 'categoria', ]
        widgets = {'consulta': Textarea(attrs={'cols': 145, 'rows': 10})}


class PreguntaForm(ModelForm):
    class Meta:
        model = Pregunta
        fields = ('resposta',)
