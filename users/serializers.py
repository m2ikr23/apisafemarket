from .models import Usuario
from rest_framework import serializers


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Usuario
        fields = ('pk','email','password','nombre','apellido','fechadenacimiento','avatar',
                    'direccion','telefono','sexo','reputacion','seguidores','status')
        