from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
# Create your views here.


class BookListApi (ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetialApi (RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all ()

    serializer_class = BookSerializer