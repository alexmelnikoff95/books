from django.urls import path

from books.views.auth import AuthView, BackOutView, PasswordResizeView, RegisterView
from books.views.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('login', AuthView.as_view(), name='login'),
    path('logout', BackOutView.as_view(), name='logout'),
    path('password_change', PasswordResizeView.as_view(), name='password_change'),

    path('register', RegisterView.as_view(), name='register')
]
