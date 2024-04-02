import re

from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer

class ValidateOTP(APIView):
    """
    validate otp and register user
    """

    def post(self, request, *args, **kwargs):
        mobile = request.data.get("mobile", None)
        otp = request.data.get("otp", None)

        # validations
        # mobile number should be 10 digits
        pattern = r"^[6789]\d{9}$"

        # Check if the phone number matches the pattern
        if not re.match(pattern, mobile):
            data = {"message": "Invalid mobile number"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        if otp != "1234":
            data = {"message": "Invalid OTP"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(mobile=mobile)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddNameEmail(APIView):
    """
    Add name and email in new user
    """

    def post(self, request, *args, **kwargs):
        id = request.data.get("id", None)
        mobile = request.data.get("mobile", None)
        name = request.data.get("name", None)
        email = request.data.get("email", None)

        # validations
        if not id or not mobile:
            data = {"message": "Bad Request"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        # if not name or not email:
        #     return Response()

        user = User.objects.filter(id=id, mobile=mobile).first()
        if not user:
            data = {"message": "Bad Request"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        user.name = name
        user.email = email
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    allowed_http_methods = ["get", "patch", "delete"]
