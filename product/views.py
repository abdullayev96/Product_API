from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework import  filters


class CategoryAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


