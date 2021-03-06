from django.urls import path, include
from . import views

urlpatterns = [
    path('/', include('infcovid.urls', namespace='infocovid')),
]