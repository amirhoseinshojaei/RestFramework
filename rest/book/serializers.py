from rest_framework import serializers
from .models import Book , Writer
from django.contrib.auth.models import User



class WriterSerializer (serializers.ModelSerializer):

    class Meta:

        model = Writer

        fields = [

            'first_name',
            'last_name',
            'writer',
        ]

class UserSerializer (serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)

class BookSerializer (serializers.ModelSerializer):
    
    writer = WriterSerializer (many = True)
    
    user = UserSerializer (many = False)
    class Meta:
        model = Book
        fields = ['book_name','publish_at','code','user']