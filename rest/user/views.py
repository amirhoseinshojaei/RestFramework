from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerialzer
# Create your views here.

class UserViewSet (viewsets.ModelViewSet):

    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerialzer
