from rest_framework.routers import DefaultRouter
from products.views import *

DRO=DefaultRouter()
DRO.register('categories',CategoryViewset,basename='categories')
DRO.register('products',ProductViewset,basename='products')

urlpatterns= DRO.urls