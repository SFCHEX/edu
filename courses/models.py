from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from ewp.models import University
# class attatchment is what we'll use to attatch content to our lectures or topics. enumerated type so we know how to embed later.

   



class attatchment(models.Model):
    class embed_type(models.TextChoices):
        GDRIVE='GD', _('gdrive')
        YOUTUBE='YT', _('youtube')
        LINK='LK', _('link')
        IMAGE='IM', _('image')

    embed_type=models.CharField(
            max_length=2,
            choices=embed_type.choices,
            default=embed_type.LINK
            )
    #will contain a link id, this will either be 33 characters long for google drive or 11 characters for youtube
    link_id=models.CharField(max_length=255)
    
class Lecture(models.Model):
    Name=models.CharField(max_length=255)
    Description=models.TextField()
    attatchments=models.ManyToManyField(attatchment,blank=True)

class Topic(models.Model):
    Name=models.CharField(max_length=255)
    Description=models.TextField()
    Lectures=models.ManyToManyField(Lecture,blank=True)

class Course(models.Model):
    Name=models.CharField(max_length=255)
    Banner=models.CharField(max_length=255)
    Institution=models.ForeignKey(University,blank=True, null=True, on_delete=models.PROTECT)
    creator= models.ForeignKey(User, on_delete=models.PROTECT)
    Description=models.TextField()
    date_added=models.DateField()
    Content= models.ManyToManyField(Topic,blank=True)


