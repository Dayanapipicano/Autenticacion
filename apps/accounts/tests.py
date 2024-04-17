from django.test import TestCase
from django.urls import reverse
from apps.accounts.forms import CustomUserCreationForm
from django.contrib.auth.models import User
from apps.accounts.views import suma




# Prueba unitaria para la función de suma
class TestSuma(TestCase):
    def test_suma(self):
        # Verifica que la suma de 1 y 2 sea 3
        self.assertEqual(suma(1, 2), 3)

        # Verifica que la suma de -1 y 1 sea 0
        self.assertEqual(suma(-1, 1), 0)

        # Verifica que la suma de 0 y 0 sea 0
        self.assertEqual(suma(0, 0), 0)

        # Verifica que la suma de números decimales funcione correctamente
        self.assertEqual(suma(2.5, 1.5), 4.0)


""" 

class RegistroTests(TestCase):
    def test_registro_get(self):
        # Prueba que el formulario de registro se muestra correctamente en una solicitud GET
        response = self.client.get(reverse('app:registro'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)

def test_registro_post_invalid(self):
    data = {
        'username': '',  # Campo obligatorio, se espera un error
        'email': 'invalid_email',  # Email inválido, se espera un error
        'password1': 'password123',
        'password2': 'password123'
    }
    response = self.client.post(reverse('app:registro'), data)
    self.assertEqual(response.status_code, 200)  # Comprueba que se muestra nuevamente el formulario
    form = response.context['form']  # Obtener el formulario del contexto de la respuesta
    self.assertFormError(response, 'form', 'username', 'Este campo es obligatorio.')  # Comprueba que se muestra un error de campo obligatorio
    self.assertFormError(response, 'form', 'email', 'Introduzca una dirección de correo electrónico válida.')  # Comprueba que se muestra un error de email inválido
    def test_registro_post_invalid(self):
        # Prueba que el formulario de registro muestra errores con datos inválidos en una solicitud POST
        data = {
            'username': '',  # Campo obligatorio, se espera un error
            'email': 'invalid_email',  # Email inválido, se espera un error
            'password1': 'password123',
            'password2': 'password123'
        }
        response = self.client.post(reverse('app:registro'), data)
        self.assertEqual(response.status_code, 200)  # Comprueba que se muestra nuevamente el formulario
        self.assertFormError(response, 'form', 'username', 'Este campo es obligatorio.')  # Comprueba que se muestra un error de campo obligatorio
        self.assertFormError(response, 'form', 'email', 'Introduzca una dirección de correo electrónico válida.')  # Comprueba que se muestra un error de email inválido
 """