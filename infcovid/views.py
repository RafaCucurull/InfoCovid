from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def consultes(request):
    return render(request, 'consultes.html')