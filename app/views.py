from django.shortcuts import render
from .models import Faunas,Usuarios,Floras,Imagenes,Parques, Parrafos
from .serializer import FaunasSerializer,UsuariosSerializer,FlorasSerializer, ImagenesSerializer, ParquesSerializer, ParrafosSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class FaunasView(APIView):
    def get(self, request):
        faunas = Faunas.objects.all()
        serializer = FaunasSerializer(faunas, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = FaunasSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def put(self, request, id_fauna):
        fauna = get_object_or_404(Parrafos, id_fauna = id_fauna)
        serializer = FaunasSerializer(fauna, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id_fauna):
        fauna = get_object_or_404(Faunas, id_fauna = id_fauna)
        fauna.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class FlorasView(APIView):
    def get(self, request):
        floras = Floras.objects.all()
        serializer = FlorasSerializer(floras, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = FlorasSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def put(self, request, id_flora):
        parrafo = get_object_or_404(Parrafos, id_flora = id_flora)
        serializer = ParrafosSerializer(parrafo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id_flora):
        flora = get_object_or_404(Floras, id_flora = id_flora)
        flora.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ImagenesView(APIView):
    def get(self, request):
        imagenes = Imagenes.objects.all()
        serializer = ImagenesSerializer(imagenes, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ImagenesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def put(self, request, id_imagen):
        imagen = get_object_or_404(Imagenes, id_imagen = id_imagen)
        serializer = ImagenesSerializer(imagen, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id_imagen):
        imagen = get_object_or_404(Imagenes, id_imagen = id_imagen)
        imagen.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class ParquesView(APIView):
    def get(self, request):
        parques = Parques.objects.all()
        serializer = ParquesSerializer(parques, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ParquesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def put(self, request, id_parque):
        parque = get_object_or_404(Parques, id_parque = id_parque)
        serializer = ParquesSerializer(parque, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id_parque):
        parque = get_object_or_404(Parques, id_parque = id_parque)
        parque.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class ParrafosView(APIView):
    def get(self, request):
        parrafos = Parrafos.objects.all()
        serializer = ParrafosSerializer(parrafos, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ParrafosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def put(self, request, id_parrafo):
        parrafo = get_object_or_404(Parrafos, id_parrafo = id_parrafo)
        serializer = ParrafosSerializer(parrafo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id_parrafo):
        parrafo = get_object_or_404(Parrafos, id_parrafo = id_parrafo)
        parrafo.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class UsuariosView(APIView):
    def get(self, request):
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializer(usuarios, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer =UsuariosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def put(self, request, id_usuario):
        usuario = get_object_or_404(Usuarios, id_usuario = id_usuario)
        serializer = UsuariosSerializer(usuario, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id_usuario):
        usuario = get_object_or_404(Usuarios, id_usuario = id_usuario)
        usuario.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class LoginView(APIView):
    def post(self, request):
        correo = request.data.get("correo")
        contraseña = request.data.get("contraseña")
        try:
            usuario = Usuarios.objects.get(correo = correo, contraseña=contraseña)
            serializer = UsuariosSerializer(usuario)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Usuarios.DoesNotExist:
            return Response({"error": "Credenciales inválida"}, status = status.HTTP_401_UNAUTHORIZED)