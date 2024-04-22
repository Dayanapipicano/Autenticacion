from django.urls import path
from .views import agregar_jugador

app_name = 'funciones'

urlpatterns = [
    #URL DE AGREGAR
    path('agregar_jugador/',agregar_jugador, name= 'agregar_jugador')
]
