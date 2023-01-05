from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

@api_view(['GET'])
def village(request):
    if request.method == 'GET':
        obj = tblvillages.objects.all()
        serializer = VillageSerializer(obj, many=True)
        return Response(serializer.data)
    # if request.method == 'POST':
    #     serializer = FoodOnlySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def villageDetail(request,uniqid):
    if request.method == 'GET':
        try:
            obj = tblvillages.objects.filter(uniqid__startswith=uniqid)
        except:
            pass
        serializer = VillageSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def district(request):
    if request.method == 'GET':
        obj = tbldistrict.objects.all()
        serializer = DistrictSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def districtDetail(request,uniqid):
    if request.method == 'GET':
        try:
            obj = tbldistrict.objects.filter(uniqid__startswith=uniqid)
        except:
            pass
        serializer = DistrictSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def communce(request):
    if request.method == 'GET':
        obj = tblcommunce.objects.all()
        serializer = CommunceSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def communceDetail(request,uniqid):
    if request.method == 'GET':
        try:
            obj = tblcommunce.objects.filter(uniqid__startswith=uniqid)
        except:
            pass
        serializer = CommunceSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def province(request):
    if request.method == 'GET':
        obj = tblprovince.objects.all()
        serializer = ProvinceSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def provinceDetail(request,uniqid):
    if request.method == 'GET':
        try:
            obj = tblprovince.objects.filter(uniqid__startswith=uniqid)
        except:
            pass
        serializer = ProvinceSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)