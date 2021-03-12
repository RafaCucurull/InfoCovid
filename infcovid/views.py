from django.shortcuts import render, redirect
from .forms import ConsultaForm
from .models import Consulta
# Create your views here.


def homepage(request):
    return render(request, 'home.html')

def consultes(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.username = request.user
            print(obj.username)
            obj.save()
            return redirect('consultes')
    else:
        form = ConsultaForm()
    return render(request, 'consultes.html', {'form': form})