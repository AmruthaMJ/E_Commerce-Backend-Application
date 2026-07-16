from django.shortcuts import render
from cart.serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CartView(viewsets.ModelViewSet):
    queryset=cart.objects.all()
    serializer_class=CartSerializer
    permission_classes=[IsAuthenticated]



    def get_queryset(self):
        return cart.objects.filter(user=self.request.user)
    

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
    