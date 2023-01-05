from rest_framework import serializers
from .models import *

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