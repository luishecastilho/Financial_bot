from django.db import models
import datetime

# Create your models here.

class Contact_Form(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    body = models.TextField()
    date = models.DateField(default=datetime.datetime.now)

    def __str__(self) -> str:
        return self.email