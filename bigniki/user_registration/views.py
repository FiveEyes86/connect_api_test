from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import *

class UserRegister(APIView):
    def get(self, request):
        lst = Users.objects.all()
        return Response({'resp': UserSerializer(lst, many=True).data})

    def post(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.create(request.data)

        return Response({'resp': user.data})
