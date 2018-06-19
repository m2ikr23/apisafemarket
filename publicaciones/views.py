from django.shortcuts import render
from .models import Publicacion,Comentario,Foto
from .serializers import PublicacionSerializer,ComentarioSerializer,FotoSerializer
from rest_framework import viewsets


class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all().order_by('pk')
    serializer_class = PublicacionSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all().order_by('pk')
    serializer_class = ComentarioSerializer

class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all().order_by('pk')
    serializer_class = FotoSerializer
    