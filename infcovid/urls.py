from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('consultes/', views.consultes, name='consultes'),
    path('consultes/personals', views.mostrarConsultes, name='consultesper'),
    path('perfil/', views.mostrarPerfil, name='perfil'),
    path('test/', views.test, name='test'),
]