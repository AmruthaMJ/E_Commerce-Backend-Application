from orders.views import *
from rest_framework.routers import DefaultRouter

DRO=DefaultRouter()
DRO.register('orders',OrderViewset,basename='orders')

urlpatterns=DRO.urls