import json

from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .filters import ProductFilter
from .paginations import CatalogPagination
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


class ReviewView(APIView):
    def post(self, request: Request, pk):
        data = request.data
        author = data["author"]
        email = data["email"]
        text = data["text"]
        rate = data["rate"]
        # date = data["date"]
        product_id = pk

        Review.objects.create(
            author=author,
            email=email,
            text=text,
            rate=rate,
            # date=date,
            product_id=product_id,
        )
        return Response(status=status.HTTP_200_OK)


class CatalogApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCatalogSerializer
    pagination_class = CatalogPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductFilter
    ordering_fields = ("rating", "price", "reviews", "date",)
