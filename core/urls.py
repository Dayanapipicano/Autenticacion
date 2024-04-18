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
from apps.funciones.views import Home, agregar_jugador, listar_jugador, editar_jugador, eliminar_jugador
from apps.accounts.views import Bienvenido, logout_view
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
from apps.accounts.views import cambio
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home, name='index'),
    
    # ENDPOINT CREAR
    #path('crear/', agregar_jugador, name='agregar_jugador'),  # No es necesario incluir 'apps.funciones.urls' aquí
    path('crear/', include('apps.funciones.urls')),
    
    # ENDPOINT LISTAR
    path('lista/', listar_jugador, name='listar_jugador'),
    path('bienvenido/', Bienvenido, name='bienvenido'),
    
    # ENDPOINT EDITAR
    path('editar/<int:id>/', editar_jugador, name='editar_jugador'),  # Añade una barra al final y nombre de la URL
    
    # ENDPOINT ELIMINAR
    path('eliminar/<int:id>/', eliminar_jugador, name='eliminar_jugador'),  # Añade una barra al final y nombre de la URL
    
    # AUTENTICACIÓN
    
    path('app/', include("apps.accounts.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', logout_view, name='logout'),
 # Añade una barra al final y nombre de la URL
    
    # Personalizar ruta y archivo html para cambiar la contraseña
    #path("cambiar-clave/", auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html"), name="password_change"),  # Añade una barra al final y nombre de la URL
    
    
    path('change', cambio, name='cambio'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset')

    #path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/password_change_done.html'), name='password_reset'),
    
    
    # path('logout/', auth_views.logout_view, name='logout'),  # Si estás usando una vista de Django para el logout, importa y utiliza la vista aquí
]

# Incluye esta línea para servir archivos estáticos durante el desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)