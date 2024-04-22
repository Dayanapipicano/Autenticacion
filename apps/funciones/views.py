from django.shortcuts import render, redirect, get_object_or_404
from .forms import JugadorForm
from .models import Jugador
from django.core.paginator import Paginator
from django.views.generic import View, TemplateView, ListView
#PAGINANA DE INICIO 
#FUNCIONES
def Home(request):
    return render(request,'index.html')

#CLASES
class TemplateView(View):
    def get(self, request, *args, **kwargs):
        pass
    
class Inicio(TemplateView):
    
    template_name = 'index.html'

#CREAR JUGADOR 
def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paginacion')
        
    else:
        form = JugadorForm()
    return render(request, 'agregar_jugador.html',{'form':form})

#LISTAR JUGADOR Y PAGINACION  

#CLASES
class listado(ListView):
    template_name = 'listar_jugador.html'
    context_object_name = 'page_obj'
    queryset = Jugador.objects.filter()

#FUNCIONES
def listar_jugador(request):
    jugadores = Jugador.objects.all()
    return render(request,'listar_jugador.html',{'jugadores':jugadores})


#PAGINACION DE JUGADORES
def Paginacion(request, jugadores=None):
    if jugadores is None:
        jugadores = Jugador.objects.all()
    paginacion = Paginator(jugadores, 10)
    #numero de pagina
    page_number = request.GET.get('page')
    page_obj = paginacion.get_page(page_number)
    return render(request, 'listar_jugador.html', {'page_obj': page_obj})


#ELIMINAR JUGADOR
def eliminar_jugador(request, id):
    #Recuperacion en base de datos
    jugador = Jugador.objects.get(id=id)
    if request.method == 'GET':
        jugador.delete()
        return redirect('paginacion')

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
        return redirect('paginacion')
    return render(request,'editar_jugador.html',{'form':form})


#FUNCION DE BUSQUEDA  
def buscar_jugadores(request):
    query = request.GET.get('q')
    jugadores = Jugador.objects.all()

    if query:
        jugadores = jugadores.filter(
            #insensibles a mayúsculas y minúsculas 
            nombre__icontains=query) | jugadores.filter(
            apellido__icontains=query)

    return Paginacion(request, jugadores)




"hoasdnkj"