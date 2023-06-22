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


class ProductImagesSerializer(serializers.ModelSerializer):
    image = SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ["image"]

    def get_image(self, obj):
        return {
            "src": obj.image.url,
            "alt": ""
        }


class ProductTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["author", "email", "text", "rate", "date"]


class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ["name", "value"]


class ProductFullSerializer(serializers.ModelSerializer):
    images = ProductImagesSerializer(many=True, read_only=True)
    # images = SerializerMethodField()
    tags = ProductTagsSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    specifications = ProductSpecificationSerializer(many=True, read_only=True)
    rating = serializers.FloatField(source="get_rating")

    class Meta:
        model = Product
        fields = ["id", "category", "price", "count", "date", "title",
                  "description", "fullDescription", "free_delivery",
                  "images", "tags", "reviews", "specifications", "rating"]

    def get_images(self, obj):
        return {
            "src": obj.image.url,
            "alt": ""
        }


class ProductCatalogSerializer(serializers.ModelSerializer):
    freeDelivery = serializers.BooleanField(source="free_delivery")
    images = ProductImagesSerializer(many=True, read_only=True)
    tags = ProductTagsSerializer(many=True, read_only=True)
    reviews = serializers.IntegerField(source="get_reviews_count")
    rating = serializers.FloatField(source="get_rating")

    class Meta:
        model = Product
        fields = [
            "id", "category", "price", "count", "date", "title", "description", "freeDelivery",
            "images", "tags", "reviews", "rating",
        ]


