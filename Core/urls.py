from django.urls import path

# LOCAL IMPORTS
from Core.views import RegisterView, LoginView

app_name = 'Core'

urlpatterns = [
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),
    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),
]
