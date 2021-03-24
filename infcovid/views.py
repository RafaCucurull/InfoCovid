from django.shortcuts import render, redirect

from users.models import CustomUser
from .forms import ConsultaForm, PreguntaForm
from .models import Consulta, Pregunta, Test


# Create your views here.


def homepage(request):
    return render(request, 'home.html')

def mascaretes(request):
    return render(request, 'mascaretes.html')


def restriccions(request):
    return render(request, 'restric.html')


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
    covid = 0;
    preguntes = Pregunta.objects.all()
    test_object = Test()
    test_object.usuari = request.user
    if request.method == 'POST':
        pregunta_1 = PreguntaForm(request.POST)
        pregunta_2 = PreguntaForm(request.POST)
        pregunta_3 = PreguntaForm(request.POST)
        if pregunta_1.is_valid() and pregunta_2.is_valid() and pregunta_3.is_valid():
            pr1 = pregunta_1.save(commit=False)
            if pr1.resposta == preguntes[0].correcta:
                covid = covid + 1
            pr2 = pregunta_2.save(commit=False)
            if pr2.resposta == preguntes[1].correcta:
                covid = covid + 1
            pr3 = pregunta_3.save(commit=False)
            if pr3.resposta == preguntes[2].correcta:
                covid = covid + 1
            if covid >= 2:
                test_object.resultat = "Positiu"
                test_object.save()
            else:
                test_object.resultat = "Negatiu"
                test_object.save()
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


def cercausuaris(request):
    email_usuari = request.GET.get('usuari')
    query = CustomUser.objects.filter(email=email_usuari)
    if len(query) == 0:
        return render(request, "nousuaris.html")
    else:
        context = {
            "object_list": query,
        }
        return render(request, "llistausuaris.html", context)
