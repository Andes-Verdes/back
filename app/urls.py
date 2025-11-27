from django.urls import path
from .views import FaunasView, FlorasView, UsuariosView, ImagenesView, ParquesView, ParrafosView, LoginView, SignUpView
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({"message": "API funcionando correctamente"})

urlpatterns = [
    path('', root_view),
    path('faunas/', FaunasView.as_view()),      #Gestion de Faunas
    path('faunas/<int:pk>/', FaunasView.as_view()),      #Gestion de Faunas por ID
    path('floras/', FlorasView.as_view()),      #Gestion de Floras
    path('floras/<int:pk>/', FlorasView.as_view()),      #Gestion de Floras por ID
    path('usuarios/', UsuariosView.as_view()),  #Gestion de Usuarios
    path('usuarios/<int:pk>/', UsuariosView.as_view()),  #Gestion de Usuarios por ID
    path('imagenes/', ImagenesView.as_view()),  #Gestion de Imagenes
    path('imagenes/<int:pk>/', ImagenesView.as_view()),  #Gestion de Imagenes por ID
    path('parques/', ParquesView.as_view()),    #Gestion de Parques
    path('parques/<int:pk>/', ParquesView.as_view()),    #Gestion de Parques por ID
    path('parrafos/', ParrafosView.as_view()),  #Gestion de Parrafos
    path('parrafos/<int:pk>/', ParrafosView.as_view()),  #Gestion de Parrafos por ID
    path('login/', LoginView.as_view()),        #Inicio de sesion (LogIn)
    path('signup/', SignUpView.as_view()),      #Registro (SignUp)
]