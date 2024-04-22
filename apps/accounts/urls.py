from django.urls import path
from django.contrib.auth import views
from . import views
from .views import simple_mail

app_name="app"
urlpatterns = [



path('profile/',views.profile,name="profile"),
path('registro/',views.registro,name="registro"),
path('logout/', views.logout_view, name='logout'),
path('mail/', simple_mail, name='password_reset'),

]

