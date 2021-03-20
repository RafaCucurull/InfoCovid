from django.shortcuts import render, redirect
from .forms import ConsultaForm, PreguntaForm
from .models import Consulta, Pregunta, Test


# Create your views here.


def homepage(request):
    return render(request, 'home.html')


def consultes(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.usuari = request.user
            obj.save()
            return redirect('consultes')
    else:
        form = ConsultaForm()
    return render(request, 'consultes.html', {'form': form})


def mostrarConsultes(request):
    queryset = Consulta.objects.filter(usuari=request.user)
    context = {
        "object_list": queryset
    }
    return render(request, 'consultespersonals.html', context)


def mostrarPerfil(request):
    return render(request, 'profile.html')


def test(request):
    preguntes = Pregunta.objects.all()
    test_object = Test()
    test_object.usuari = request.user
    test_object.save()
    if request.method == 'POST':
        pregunta_1 = PreguntaForm(request.POST)
        pregunta_2 = PreguntaForm(request.POST)
        pregunta_3 = PreguntaForm(request.POST)
        if pregunta_1.is_valid() and pregunta_2.is_valid() and pregunta_3.is_valid() :
            pregunta_1.save()
            pregunta_2.save()
            pregunta_3.save()
            return redirect('test')
    else:
        pregunta_1 = PreguntaForm()
        pregunta_2 = PreguntaForm()
        pregunta_3 = PreguntaForm()
    context = {
        "object_list": preguntes,
        'pregunta_1': pregunta_1,
        'pregunta_2': pregunta_2,
        'pregunta_3': pregunta_3,
    }
    return render(request, 'test.html', context)
