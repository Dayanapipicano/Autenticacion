from django.shortcuts import render, redirect, get_object_or_404
from .forms import JugadorForm
from .models import Jugador
from django.core.paginator import Paginator
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
#PAGINANA DE INICIO 
# VISTA PRINCIPAL POR FUNCIONES
def Home(request):
    return render(request,'index.html')

#VISTA PRINCIPAL POR CLASES
#clase padre
class TemplateView(View):
    def get(self, request, *args, **kwargs):
        pass
    
#renderizar el template
class Inicio(TemplateView):
    
    template_name = 'index.html'

#CREAR JUGADOR POR FUNCION
def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paginacion')
        
    else:
        form = JugadorForm()
    return render(request, 'agregar_jugador.html',{'form':form})

#CREAR JUGADOR POR CLASE

class CreateJudador(CreateView):
    model = Jugador
    template_name = 'agregar_jugador.html'
    form_class =  JugadorForm
    success_url=reverse_lazy('paginacion')
    



# CREAR LISTA POR CLASES
class listado(ListView):
    
    template_name = 'listar_jugador.html'
    context_object_name = 'page_obj'
    queryset = Jugador.objects.filter()
    

#CREAR LISTA POR FUNCIONES
def listar_jugador(request):
    jugadores = Jugador.objects.all()
    return render(request,'listar_jugador.html',{'jugadores':jugadores})


#PAGINACION DE JUGADORES
def Paginacion(request, jugadores=None):
    #se proporciono lista de jugadores, si o no?
    if jugadores is None:
        jugadores = Jugador.objects.all()
    paginacion = Paginator(jugadores, 10)
    #numero de pagina
    page_number = request.GET.get('page')
    page_obj = paginacion.get_page(page_number)
    return render(request, 'listar_jugador.html', {'page_obj': page_obj})


#ELIMINAR JUGADOR POR FUNCIONES
def eliminar_jugador(request, id):
    #Recuperacion en base de datos
    jugador = Jugador.objects.get(id=id)
    if request.method == 'GET':
        jugador.delete()
        return redirect('paginacion')
    
#ELIMINAR POR CLASE
class Eliminar(DeleteView):
    
    model = Jugador
    success_url = reverse_lazy('paginacion')
    
#EDITAR JUGADOR POR FUNCIONES
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

#ACTUALIZAR POR CLASES
class Actualizar(UpdateView):
    model = Jugador
    template_name = 'editar_jugador.html'
    from_class = JugadorForm
    fields = ['nombre','apellido']
    #se ejecuta de manera mas perezosa despues de que esten todos los componentes cargados (redireccion)
    success_url = reverse_lazy('paginacion')

#FUNCION DE BUSQUEDA  
def buscar_jugadores(request):
    query = request.GET.get('q')
    jugadores = Jugador.objects.all()
    
    #se proporciono valor en la consulta
    if query:
        jugadores = jugadores.filter(
            #insensibles a mayúsculas y minúsculas, valores que obtenga la consulta query
            nombre__icontains=query) | jugadores.filter(
            apellido__icontains=query)

    return Paginacion(request, jugadores)




