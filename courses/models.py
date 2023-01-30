from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# class attatchment is what we'll use to attatch content to our lectures or topics. enumerated type so we know how to embed later.

   


class attatchment(models.Model):
    class embed_type(models.TextChoices):
        GDRIVE='GD', _('gdrive')
        YOUTUBE='YT', _('youtube')

    embed_type=models.CharField(
            max_length=2,
            choices=embed_type.choices,
            default=embed_type.GDRIVE
            )
    #will contain a link id, this will either be 33 characters long for google drive or 11 characters for youtube
    link_id=models.CharField(max_length=50)
    
class Lecture(models.Model):
    Name=models.CharField(max_length=255)
    attatchments=models.ForeignKey(attatchment,on_delete=models.CASCADE)

class Topic(models.Model):
    Name=models.CharField(max_length=255)
    Description=models.TextField()
    attachments=models.ForeignKey(Lecture,on_delete=models.CASCADE)

 
class CourseContent(models.Model):
    topics=models.ForeignKey(Topic,on_delete=models.CASCADE)


class Course(models.Model):
    Name=models.CharField(max_length=255)
    creator= models.ForeignKey(User, on_delete=models.PROTECT)
    Description=models.TextField()
    date_added=models.DateField()
    Content= models.ForeignKey(CourseContent, on_delete=models.CASCADE)


