import json

from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from .models import Profile
from .serializers import ProfileSerializer

from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request


class SingInView(APIView):
    def post(self, request):
        user_data = json.loads(request.body)
        username = user_data.get("username")
        password = user_data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignUpView(APIView):
    def post(self, request: Request):
        user_data = json.loads(request.body)
        username = user_data.get("username")
        password = user_data.get("password")
        fullname = user_data.get("name")
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


class ProfileView(APIView):
    def get(self, request):
        profile = Profile.objects.filter(user_id=request.user.id)
        return Response(ProfileSerializer(profile, many=True).data[0])

    def post(self, request):
        profile = Profile.objects.filter(user_id=request.user.id)
        data = request.data
        fullname = data.get("fullName")
        email = data.get("email")
        phone = data.get("phone")
        profile.update(
            fullname=fullname,
            email=email,
            phone=phone,
        )
        return Response(ProfileSerializer(profile, many=True).data[0])


# class ProfileView(ListAPIView):
#     serializer_class = ProfileSerializer
#
#     def get_queryset(self):
#         return Profile.objects.filter(user_id=self.request.user.id)
#
#     def get_paginated_response(self, data):
#         return Response(data)
#
#
# class ProfileUpdateView(UpdateAPIView):
#     serializer_class = ProfileSerializer
#
#     def get_queryset(self):
#         return Profile.objects.filter(user_id=self.request.user.id)
#
#     def get_paginated_response(self, data):
#         return Response(data)

#fix
class ProfilePasswordView(APIView):
    def post(self, request):
        data = request.data
        curr_pass = data.get("currentPassword")
        new_pass = data.get("newPassword")
        print(new_pass, curr_pass)
        user: User = request.user
        if user.check_password(curr_pass):
            user.set_password(new_pass)
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
