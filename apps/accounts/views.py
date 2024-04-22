from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as make_login
from django.urls import reverse
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, UserPerfilform
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import UserPerfil
import os
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.core.mail import send_mail



def Bienvenido(request):
    return render(request, 'index.html')



def cambio(request):
    return render(request, 'registration/password_reset_form.html')

def registro(request):
    if request.method == "POST": 
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                # Redireccionar al usuario a la página de inicio de sesión
                return redirect('login')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'registro.html', {'form': form})

@login_required 
def profile(request):
    form=UserPerfilform()
    if request.method == "POST":
        try: #avatar anterior
            Userperfil = UserPerfil.objects.get(user=request.user)
            form=UserPerfilform(request.POST, request.FILES,instance=Userperfil)
            #eliminar el avatar anterior, otenemos el path
            pathAvatarViejo=os.path.join(settings.MEDIA_ROOT,Userperfil.avatar.name)
        except ObjectDoesNotExist:
            form = UserPerfilform(request.POST,request.FILES)
            
        if form.is_valid():
            #preguntamos si existe el avatar viejo
            if pathAvatarViejo is not None and os.path.isfile(pathAvatarViejo):
                os.remove(pathAvatarViejo)
                
            userProfile= form.save(commit=False)
            userProfile.user=request.user
            userProfile.save()

    return render(request, 'registration/profile.html', {'form':form})

#envio de correo electronico
def simple_mail(request):
    
    if request.method == 'POST':
        # Obtener la dirección de correo electrónico del formulario
        recipient_email = request.POST.get('email')

        # Verificar si se proporcionó una dirección de correo electrónico válida
        if recipient_email:
            # Enviar el correo electrónico con la dirección de correo electrónico del formulario como destinatario
            send_mail(
                subject='Cambio de contraseña',
                message='Confirmas el cambio de contraseña',
                from_email='nova@gmail.com',
                recipient_list=[recipient_email],
            )
            return HttpResponse('Correo enviado exitosamente')
        else:
            return HttpResponse('La dirección de correo electrónico no se proporcionó correctamente')
    else:
        return HttpResponse('El formulario debe ser enviado utilizando el método POST')

#cierre de session 
def logout_view(request):
    logout(request)
    return redirect('login')





#EJEMPLO DE TEST

def suma(a, b):
    return a + b


#VISTA BASADA EN CLASE
