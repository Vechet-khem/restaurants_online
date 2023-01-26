from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

@api_view(['GET'])
def user(request):
    if request.method == 'GET':
        obj = User.objects.all()
        serializer = UserSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)