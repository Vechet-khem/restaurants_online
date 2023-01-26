from rest_framework import serializers
from .models import *
from django.conf import settings

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblvillages
        fields = ('uniqid','khmer','english')

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbldistrict
        fields = ('uniqid','khmer','english')

class CommunceSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblcommunce
        fields = ('uniqid','khmer','english')

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblprovince
        fields = ('uniqid','khmer','english')

class SupplyerSerializer(serializers.ModelSerializer):
    village = VillageSerializer(read_only = True)
    province = ProvinceSerializer(read_only = True)
    commune = CommunceSerializer(read_only = True)
    district = DistrictSerializer(read_only = True)
    image = serializers.CharField(source='get_image_url',read_only = True)

    class Meta:
        model = tblsupplyer
        fields = ('id','first_name','last_name','email','mobile','company_name','province','district','commune','village','image')

class SupplyerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblsupplyer
        fields = ('id','first_name','last_name','email','mobile','company_name','province','district','commune','village','image')

class CustomerSerializer(serializers.ModelSerializer):
    village = VillageSerializer(read_only = True)
    province = ProvinceSerializer(read_only = True)
    commune = CommunceSerializer(read_only = True)
    district = DistrictSerializer(read_only = True)
    image = serializers.CharField(source='get_image_url',read_only = True)

    class Meta:
        model = tblcustomer
        fields = ('id','first_name','last_name','email','mobile','province','district','commune','village','image')

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblcustomer
        fields = ('id','first_name','last_name','email','mobile','province','district','commune','village','image')
