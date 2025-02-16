# DJANGO IMPORTS
from django.views.generic import TemplateView


class RegisterView(TemplateView):
    template_name = 'Core/register.html'


class LoginView(TemplateView):
    template_name = 'Core/login.html'
