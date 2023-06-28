from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    avatar = SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "fullname", "email", "phone", "avatar"
        ]

    def get_avatar(self, obj):
        if obj.avatar:
            return {
                "src": obj.avatar.url,
                "alt": ""
            }
        return {
            "src": "",
            "alt": ""
        }
