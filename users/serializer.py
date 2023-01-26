from rest_framework import serializers
from .models import *
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','contact','image','is_staff','is_superuser','input_date')