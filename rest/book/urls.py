from django.urls import path
from . import views

urlpatterns = [
    path ('',views.BookListApi.as_view(),name= 'book_list'),
]