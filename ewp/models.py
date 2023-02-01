from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Members(models.Model):
    Member= models.ForeignKey(User, on_delete=models.PROTECT)

class University(models.Model):
    Name=models.CharField(max_length=255)
    Email=models.CharField(max_length=255)
    Banner=models.CharField(max_length=255)
    attatchments=models.ForeignKey(Members,on_delete=models.CASCADE)



