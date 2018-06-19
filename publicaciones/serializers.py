from .models import Publicacion,Comentario,Foto
from rest_framework import serializers


class PublicacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Publicacion 
        fields = ('autor','categoria','descripcion','precio')


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Comentario
        fields = ('autor','comentario','publicacion')


class FotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Foto
        fields = ('publicacion','foto')