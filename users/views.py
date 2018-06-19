from django.shortcuts import render
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import viewsets


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('pk')
    serializer_class = UsuarioSerializer
    