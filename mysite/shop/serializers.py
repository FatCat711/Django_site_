from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import *


class SubCategorySerializer(serializers.ModelSerializer):
    image = SerializerMethodField()
    class Meta:
        model = SubCategory
        fields = ["id", "title", "image"]

    def get_image(self, obj):
        return {
            "src": obj.image.url,
            "alt": ""
        }


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)
    image = SerializerMethodField()
    class Meta:
        model = Category
        fields = ["id", "title", "image", "subcategories"]

    def get_image(self, obj):
        return {
            "src": obj.image.url,
            "alt": ""
        }