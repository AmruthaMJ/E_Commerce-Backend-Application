from django.shortcuts import render
from orders.serializers import *
from orders.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
# Create your views here.



class OrderViewset(viewsets.ModelViewSet):
    serializer_class=OrderSerializers
    permission_classes=[IsAuthenticated]


    def get_queryset(self):

        if self.request.user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
