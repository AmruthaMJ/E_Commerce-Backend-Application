from rest_framework import serializers
from orders.models import *

class OrderItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model=OrderItems
        fields='__all__'


class OrderSerializers(serializers.ModelSerializer):
    items=OrderItemsSerializers(
        many=True,
        read_only=True
    )

    class Meta:
        model=Order
        fields='__all__'
        read_only_fields=['user','status']
        