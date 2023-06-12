from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *


# class CategoryApiView(APIView):
#     def get(self, request):
#         category = Category.objects.all()
#         sub_category = SubCategory.objects.all()
#
#         return Response()


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.prefetch_related("subcategories")
    serializer_class = CategorySerializer

    def get_paginated_response(self, data):
        return Response(data)
