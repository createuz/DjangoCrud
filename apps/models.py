from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    gmail = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    birthday = models.DateField()
    image = models.ImageField(upload_to='photo/')

    def __str__(self):
        return self.username
