from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Customer(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=20, default="1234")

    def __str__(self):
        return self.name
