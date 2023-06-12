from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = "shop"

routers = DefaultRouter()
# routers.register("categories", CategoryViewSet)

urlpatterns = [
    path("api/", include(routers.urls)),
    path("api/categories/", CategoryViewSet.as_view({'get': 'list'})),
]
