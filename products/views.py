from django.shortcuts import render
from products.serializers import *
from products.models import *
from rest_framework import viewsets

# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerailaizer


class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer