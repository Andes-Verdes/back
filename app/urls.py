from django.urls import path
from .views import FaunasView, FlorasView, UsuariosView

urlpatterns = [
    path('faunas/', FaunasView.as_view()),
    path('floras/', FlorasView.as_view()),
    path('usuarios/',UsuariosView.as_view())
]