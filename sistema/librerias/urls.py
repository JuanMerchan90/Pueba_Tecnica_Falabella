from django.urls import path
from . import views

urlpatterns = [
    #path('', views.inicio, name= 'inicio'),
    path('', views.base, name= 'base'),
    #path('Inicio', views.inicio, name='Inicio')
]


