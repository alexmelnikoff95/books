from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from books.forms import UserRegisterForm


class AuthView(LoginView):
    template_name = 'registration/login.html'
    next_page = '/'


class BackOutView(LogoutView):
    next_page = '/'


class PasswordResizeView(PasswordChangeView):
    success_url = reverse_lazy('index')
    template_name = 'registration/password_resize.html'


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
