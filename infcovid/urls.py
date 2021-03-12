from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('consultes/', views.consultes, name='consultes'),
]