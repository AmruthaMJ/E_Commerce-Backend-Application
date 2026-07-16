from cart.models import *
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=cart
        fields='__all__'
        read_only_fields = ['user']
        