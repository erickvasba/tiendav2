from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.http import HttpResponse


from app_f.models import *

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from app_f.serializers import *

from rest_framework import generics
from rest_framework.response import Response


def index(request):
    return HttpResponse("main")


class Crear_producto_view(CreateView):

    model = Producto
    template_name = 'app_F/crear_producto.html'
    fields = ['producto_nombre', 'producto_marca', 'producto_modelo',
              'producto_precio', 'producto_calificacion']


class Modificar_producto_view(UpdateView):
    model = Producto
    template_name = 'app_f/modificar_producto.html'
    fields = ['producto_nombre', 'producto_marca', 'producto_modelo',
              'producto_precio', 'producto_calificacion']


class Borrar_producto_view(DeleteView):
    model = Producto
    template_name = 'app_f/borrar_producto.html'

# USER


class Crear_user(CreateView):
    model = Profile
    template_name = 'app_f/crear_user.html'
    fields = ['username', 'password']


class Modificar_user(UpdateView):
    model = Profile
    template_name = 'app_f/modificar_user.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'password']


class Borrar_user(DeleteView):
    model = Profile
    template_name = 'app_f/borrar_user.html'


# REST GENERICS

# PRODCUTOS
class ProductoList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Producto.objects.all()
    serializer_class = Producto_Ser


class ProductoCreate(generics.CreateAPIView):
    serializer_class = Producto_Ser


class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = Producto_Ser
# PRODCUTOS
# PRODUCTOS FOTOS


class FotoProductoList(generics.ListAPIView):
    queryset = Foto_producto.objects.all()
    serializer_class = Foto_producto_Ser


class FotoProductoCreate(generics.CreateAPIView):
    serializer_class = Foto_producto_Ser


class FotoProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foto_producto.objects.all()
    serializer_class = Foto_producto_Ser

# PRODUCTOS FOTOS


# USER


class UserList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = User_Ser


class UserCreate(generics.CreateAPIView):
    serializer_class = User_Ser


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = User_Ser


# USER
