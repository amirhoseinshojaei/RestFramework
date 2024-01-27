from django.urls import path
from . import views

urlpatterns = [
    path ('',views.BookListApi.as_view(),name= 'book_list'),

    path ('<int:pk>/' , views.BookDetialApi.as_view(), name= 'book-detail'),
]