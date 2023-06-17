from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.prefetch_related("subcategories")
    serializer_class = CategorySerializer

    def get_paginated_response(self, data):
        return Response(data)


class ProductFullViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer

    def get_paginated_response(self, data):
        return Response(data)


class ReviewViewSet(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "pk"

