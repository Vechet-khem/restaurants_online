from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

@api_view(['GET','POST'])
def user(request):
    if request.method == 'GET':
        obj = User.objects.all()
        serializer = UserSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserDetailSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            newObj = User.objects.get(id = serializer.data['id'])
            serializer1 = UserSerializer(newObj)
            return Response(serializer1.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)