from django.urls import path
from .views import FaunasView, FlorasView, UsuariosView, ImagenesView, ParquesView, ParrafosView, LoginView, SignUpView

urlpatterns = [
    path('faunas/', FaunasView.as_view()),      #Gestion de Faunas
    path('floras/', FlorasView.as_view()),      #Gestion de Floras
    path('usuarios/', UsuariosView.as_view()),  #Gestion de Usuarios
    path('imagenes/', ImagenesView.as_view()),  #Gestion de Imagenes
    path('parques/', ParquesView.as_view()),    #Gestion de Parques
    path('parrafos/', ParrafosView.as_view()),  #Gestion de Parrafos
    path('login/', LoginView.as_view()),        #Inicio de sesion (LogIn)
    path('signup/', SignUpView.as_view()),      #Registro (SignUp)
]