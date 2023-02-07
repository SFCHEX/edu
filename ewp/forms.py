from django import forms
from courses.models import *
from django.forms import (
    Textarea
)

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course 
        exclude =['Institution','creator','Content','date_added']

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic 
        exclude =['Lectures']
        widgets={
            'Description': Textarea(attrs={'rows': 1, 'cols': 5})
        }




class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture 
        exclude =[]


class AttachmentsForm(forms.ModelForm):
    class Meta:
        model = attatchment 
        exclude =['Institution','creator','Content','date_added']