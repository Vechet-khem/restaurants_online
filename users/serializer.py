from rest_framework import serializers
from food_menu.serializer import *
from .models import *
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    village = VillageSerializer(read_only = True)
    commune = CommunceSerializer(read_only = True)
    district = DistrictSerializer(read_only = True)
    province = ProvinceSerializer(read_only = True)
    image = serializers.CharField(source='get_image_url',read_only = True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name','username','password','email','contact','image','is_staff','is_superuser','village','commune','district','province','input_date')

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username','password','email','contact','image','is_staff','is_superuser','village','commune','district','province')