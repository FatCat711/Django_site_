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
    path("api/product/<pk>/reviews", ReviewView.as_view()),
    path("api/catalog/", CatalogApiView.as_view()),
    path("api/products/popular/", CatalogPopularAPIView.as_view()),
    path("api/products/limited/", CatalogLimitedAPIView.as_view()),
    path("api/tags/", TagAPIView.as_view()),
]
