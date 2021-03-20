from django import forms
from django.forms import ModelForm, Textarea
from infcovid.models import Consulta, Pregunta


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['consulta', 'categoria', ]
        widgets = {'consulta': Textarea(attrs={'cols': 145, 'rows': 10})}


class PreguntaForm(ModelForm):
    choice_field = forms.MultipleChoiceField(choices=Pregunta.RESPOSTA_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Pregunta
        fields = ('choice_field',)
