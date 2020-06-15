from rest_framework import serializers


from app_f.models import *


class User_Ser(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'password', 'first_name',
                  'last_name', 'email', 'celular', 'direccion', 'ciudad']


class Producto_Ser(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['id', 'producto_nombre', 'producto_marca', 'producto_modelo',
                  'producto_precio', 'producto_calificacion', 'producto_fecha_creacion']


class Foto_producto_Ser(serializers.ModelSerializer):

    class Meta:
        model = Foto_producto
        fields = ['id', 'producto', 'foto_foto',
                  'foto_foto2', 'foto_descripcion']
