from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, ValidateOTP, AddNameEmail

router = DefaultRouter()

router.register("accounts", UserViewSet, basename="accounts")

urlpatterns = [
    path('', include(router.urls)),
    path("validate_otp/", ValidateOTP.as_view(), name="validate_otp"),
    path("add_name_email/", AddNameEmail.as_view(), name="add_name_email"),
]
