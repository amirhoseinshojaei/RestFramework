from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User


class UserSerializer (serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)

class BookSerializer (serializers.ModelSerializer):
    
    user = UserSerializer (many = False)
    class Meta:
        model = Book
        fields = ['book_name','publish_at','code','user']