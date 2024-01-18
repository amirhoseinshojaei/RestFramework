from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin (admin.ModelAdmin):

    list_display = [
        'book_name',
        'publish_at',
        'user'
    ]

    list_filter = [
        'user',
        'publish_at'
    ]

    search_fields = ['book_name']

    date_hierarchy = 'publish_at'

admin.site.register (Book,BookAdmin)