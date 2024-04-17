from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from .models import UserPerfil

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico", max_length=50, help_text="Coloca tu correo electrónico", error_messages={'invalid': 'Solo puedes colocar caracteres válidos para el email'})

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("El correo electrónico ya ha sido tomado")
        return email

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data["username"],
            self.cleaned_data["email"],
            self.cleaned_data["password1"],
        )
        return user

class UserPerfilform(forms.ModelForm):
    class Meta:
        model = UserPerfil
        fields = ("avatar", "user")
        
    def __init__(self, *args, **kwargs):
        super(UserPerfilform, self).__init__(*args, **kwargs)
        self.fields["user"].widget = forms.HiddenInput()
        self.fields["user"].required = False
        
    def clean_avatar(self):
        avatar = self.cleaned_data["avatar"]
        
        w, h = get_image_dimensions(avatar)
        
        max_width = 500
        max_height = 500
        
        if w > max_width or h > max_height:
            raise forms.ValidationError("La imagen no puede superar los %spx, %spx"%(max_width, max_height))
        
        m, t = avatar.content_type.split("/")
        
        if not (m == 'image' and t in ["jpeg", "jpg", "gif", "png"]):
            raise forms.ValidationError("Imagen muy pesada")
        
        return avatar
