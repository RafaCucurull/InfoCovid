from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('mascaretes/', views.infomascaretes, name="mascaretes"),
    path('informacio/', views.infogeneral, name="infogeneral")
]