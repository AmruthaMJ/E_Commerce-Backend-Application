from django.shortcuts import render
from products.serializers import *
from products.models import *
from rest_framework import viewsets
from products.permissions import *

# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerailaizer
    permission_classes=[IsAdminOrReadOnly]


class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAdminOrReadOnly]