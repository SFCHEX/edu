from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()        #leave the content as text for starters
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('ewp-archive')
