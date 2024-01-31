from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.utils import timezone
# Create your models here.

class Book (models.Model):

    book_name = models.CharField (max_length = 255)

    publish_at = models.DateTimeField (auto_now = True , auto_now_add = False)

    description = models.TextField (max_length = 1500)

    code = models.CharField (max_length = 50 , default = get_random_string(length= 50))

    user = models.ForeignKey (User , null = True ,on_delete = models.SET_NULL ,)

    

class Writer (models.Model):

    first_name = models.CharField (max_length=32)

    last_name = models.CharField (max_length = 32)

    user = models.ForeignKey(User , on_delete= models.CASCADE)

    publish_at = models.DateTimeField (default= timezone.now )

    book = models.ManyToManyField (Book, related_name= 'writers')