from django.shortcuts import render
from accounts.models import *
from accounts.serializers import *
from rest_framework.generics import CreateAPIView

# Create your views here.

class RegisterView(CreateAPIView):
    QS=User.objects.all()
    serializer_class=AccountSerializers
