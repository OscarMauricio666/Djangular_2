from django.shortcuts import render

from rest_framework.response import Response
from .serializaers import UserSerializers
from rest_framework.views import APIView
from rest_framework import status


class UserApi(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)  # aca viene la data
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
