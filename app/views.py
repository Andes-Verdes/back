from django.shortcuts import render
from .models import Faunas,Usuarios,Floras
from .serializer import FaunasSerializer,UsuariosSerializer,FlorasSerializer
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
    
class FlorasView(APIView):
    def get(self, request):
        floras = Floras.objects.all()
        serializer = FlorasSerializer(floras, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = FlorasSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

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