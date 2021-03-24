from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def infomascaretes(request):
    return render(request, 'mascaretes.html')

def infogeneral(request):
    return render(request, 'informacio_general.html')