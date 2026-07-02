from rest_framework import serializers
from accounts.models import *



class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password','phone','address']

        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

