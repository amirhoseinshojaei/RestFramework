from django.contrib import admin
from .models import Book , Writer
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

class WritersAdmin (admin.ModelAdmin):

    list_display = [

        'first_name',
        'last_name',
        'user',
        'publish_at'
    ]

   

    list_select_related =['user']

    

    list_filter = [

        'user',
        'publish_at'
    ]

    list_per_page = 5

    search_fields = ['first_name','last_name','user']

    date_hierarchy = 'publish_at'

admin.site.register(Writer,WritersAdmin)

