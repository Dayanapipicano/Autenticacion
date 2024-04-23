"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.funciones.views import Home, agregar_jugador, editar_jugador, eliminar_jugador,buscar_jugadores, Paginacion
from apps.accounts.views import Bienvenido, logout_view,cambio
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from apps.funciones.views import Inicio, listado, Actualizar,CreateJudador,Eliminar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home, name='home'),
    path('clases/', Inicio.as_view(), name='clases'),
    # ENDPOINT CREAR
    #path('crear/', agregar_jugador, name='agregar_jugador'),  # No es necesario incluir 'apps.funciones.urls' aquí
    path('crear/', include('apps.funciones.urls')),
    path('agregar/', CreateJudador.as_view(), name='agregar'),
    
    # ENDPOINT LISTAR
    path('lista/', listado.as_view(), name='listar_jugador'),
    path('bienvenido/', Bienvenido, name='bienvenido'),
    
    # ENDPOINT EDITAR
    path('editar/<int:id>/', editar_jugador, name='editar_jugador'),  
    path('actualizar/<int:pk>/', Actualizar.as_view(), name='actualizar'),  
    
    # ENDPOINT ELIMINAR
    path('eliminar/<int:id>/', eliminar_jugador, name='eliminar_jugador'), 
    path('delete/<int:pk>', Eliminar.as_view(), name='eliminar'),
    
    # AUTENTICACIÓN
    
    path('app/', include("apps.accounts.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    
    #CIERRE DE SESSION
    path('logout/', logout_view, name='logout'),
    
    #CAMBIO DE CONTRASEÑA
    path('change', cambio, name='cambio'),
    #path('reset-password/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),

    #PAGINACION Y BUSCADOR
    path('buscar/', buscar_jugadores, name='buscar_jugadores'),
    path('paginacion/', Paginacion, name='paginacion'),
    

]

# Incluye esta línea para servir archivos estáticos durante el desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)