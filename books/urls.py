from django.urls import path

from books.views import ArtistListView, \
    ArtistDetailView
from books.views.auth import AuthView, BackOutView, PasswordResizeView, RegisterView
from books.views.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('artist_list', ArtistListView.as_view(), name='artist_list'),
    path('<int:pk>', ArtistDetailView.as_view(), name='artist_detail'),

    path('login', AuthView.as_view(), name='login'),
    path('logout', BackOutView.as_view(), name='logout'),
    path('password_change', PasswordResizeView.as_view(), name='password_change'),

    path('register', RegisterView.as_view(), name='register')
]
