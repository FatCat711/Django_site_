from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = "shop"

routers = DefaultRouter()
routers.register(r"product", ProductFullViewSet)
# routers.register(r"product/<pk>/review", ReviewViewSet)

urlpatterns = [
    path("api/", include(routers.urls)),
    path("api/categories/", CategoryViewSet.as_view({'get': 'list'})),
    path("api/product/<pk>/reviews", ReviewViewSet.as_view()),
    # path("api/product/<id>/", ProductFullViewSet.as_view({'get': 'list'})),
]
