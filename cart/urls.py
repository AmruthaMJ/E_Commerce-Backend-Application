from rest_framework.routers import DefaultRouter
from cart.views import *

DRO=DefaultRouter()
DRO.register('cart',CartView,basename='cart')

urlpatterns=DRO.urls