from django.shortcuts import render
from .models import Faunas,Usuarios,Floras,Imagenes,Parques, Parrafos
from .serializer import FaunasSerializer,UsuariosSerializer,FlorasSerializer, ImagenesSerializer, ParquesSerializer, ParrafosSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class FaunasView(APIView):
    def get(self, request):
        faunas = Faunas.objects.all()
        serializer = FaunasSerializer(faunas, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = FaunasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def delete(self, request, id_fauna):
        try:
            fauna = Faunas.objects.get(id_fauna = id_fauna)
            fauna.delete()
            return Response(status = 204)
        except Faunas.DoesNotExist:
            return Response(status = 404)
    
class FlorasView(APIView):
    def get(self, request):
        floras = Floras.objects.all()
        serializer = FlorasSerializer(floras, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = FlorasSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)
    def delete(self, request, id_flora):
        try:
            flora = Floras.objects.get(id_flora = id_flora)
            flora.delete()
            return Response(status = 204)
        except Floras.DoesNotExist:
            return Response(status = 404)

class ImagenesView(APIView):
    def get(self, request):
        imagenes = Imagenes.objects.all()
        serializer = ImagenesSerializer(imagenes, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ImagenesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)
    def delete(self, request, id_imagen):
        try:
            imagen = Imagenes.objects.get(id_imagen = id_imagen)
            imagen.delete()
            return Response(status = 204)
        except Imagenes.DoesNotExist:
            return Response(status = 404)
    
class ParquesView(APIView):
    def get(self, request):
        parques = Parques.objects.all()
        serializer = ParquesSerializer(parques, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ParquesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)
    def delete(self, request, id_parque):
        try:
            parque = Parques.objects.get(id_parque = id_parque)
            parque.delete()
            return Response(status = 204)
        except Parques.DoesNotExist:
            return Response(status = 404)
    
class ParrafosView(APIView):
    def get(self, request):
        parrafos = Parrafos.objects.all()
        serializer = ParrafosSerializer(parrafos, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ParrafosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)
    def delete(self, request, id_parrafo):
        try:
            parrafo = Parrafos.objects.get(id_parrafo = id_parrafo)
            parrafo.delete()
            return Response(status = 204)
        except Parrafos.DoesNotExist:
            return Response(status = 404)
    
class UsuariosView(APIView):
    def get(self, request):
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializer(usuarios, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer =UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= 201)
        return Response(serializer.errors, status=400)
    def delete(self, request, id_usuario):
        try:
            usuario = Usuarios.objects.get(id_usuario = id_usuario)
            usuario.delete()
            return Response(status = 204)
        except Usuarios.DoesNotExist:
            return Response(status = 404)