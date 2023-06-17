import json

from django.contrib.auth.models import User

from .models import Profile

from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request


class SingInView(APIView):
    def post(self, request):
        user_data = json.loads(request.body)
        username = user_data["username"]
        password = user_data["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignUpView(APIView):
    def post(self, request: Request):
        user_data = json.loads(request.body)
        username = user_data["username"]
        password = user_data["password"]
        fullname = user_data["name"]
        user_up = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user_up, fullname=fullname)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LogoutView(APIView):
    def post(self, request: Request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

