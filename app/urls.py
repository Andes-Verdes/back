from django.urls import path
from .views import FaunasView, FlorasView, UsuariosView, ImagenesView, ParquesView, ParrafosView

urlpatterns = [
    path('faunas/', FaunasView.as_view()),
    path('floras/', FlorasView.as_view()),
    path('usuarios/', UsuariosView.as_view()),
    path('imagenes/', ImagenesView.as_view()),
    path('parques/', ParquesView.as_view()),
    path('parrafos/', ParrafosView.as_view()),
]