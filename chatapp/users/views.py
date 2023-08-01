from django.shortcuts import render
from .serializers import SignUpSerializer, UserSerializer
from .models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

# Create your views here.

# 회원가입
@permission_classes([AllowAny])
class SignUp(APIView):

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

