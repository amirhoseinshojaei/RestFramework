from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.


class BookListApi (ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer