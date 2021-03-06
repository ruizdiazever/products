from django.shortcuts import render

# Para consumir la API es necesario este paso..
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets


class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


