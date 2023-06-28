from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = "auth"

routers = DefaultRouter()
# routers.register("", )

urlpatterns = [
    path("api/", include(routers.urls)),
    path("api/sign-in", SingInView.as_view(), name="login"),
    path("api/sign-up", SignUpView.as_view(), name="register"),
    path("api/sign-out", LogoutView.as_view(), name="logout"),
    path("api/profile", ProfileView.as_view()),
    path("api/profile/password", ProfilePasswordView.as_view()),
]
