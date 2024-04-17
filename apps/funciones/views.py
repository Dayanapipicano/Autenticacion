from django.shortcuts import render, redirect, get_object_or_404
from .forms import JugadorForm
from .models import Jugador
def Home(request):
    return render(request,'index.html')

#CREAR JUGADOR 
def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_jugador')
        
    else:
        form = JugadorForm()
    return render(request, 'agregar_jugador.html',{'form':form})

#LISTAR JUGADOR 
def listar_jugador(request):
    jugadores = Jugador.objects.all()
    return render(request,'listar_jugador.html',{'jugadores':jugadores})

#ELIMINAR JUGADOR
def eliminar_jugador(request, id):
    #Recuperacion en base de datos
    jugador = Jugador.objects.get(id=id)
    if request.method == 'GET':
        jugador.delete()
        return redirect('listar_jugador')

#EDITAR JUGADOR
def editar_jugador(request,id):
    
    
    jugador = Jugador.objects.get(id=id)
    #cuando voy al formulario
    if request.method =='GET':
        #SE CREA UN FORMULARIO DE TIPO JUGADOR
       form = JugadorForm(instance=jugador)
    #cuando edito
    else:
        #SE VERIFICA SI EL FORMULARIO ES VALIDO
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
        return redirect('listar_jugador')
    return render(request,'editar_jugador.html',{'form':form})

