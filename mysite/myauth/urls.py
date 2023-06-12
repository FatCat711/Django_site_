from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import *

app_name = "auth"

routers = DefaultRouter()
# routers.register("", )

urlpatterns = [
    path("api/", include(routers.urls)),
]
