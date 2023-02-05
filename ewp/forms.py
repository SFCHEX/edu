from django import forms
from courses.models import *
from django.forms.models import (
    inlineformset_factory,
    modelformset_factory,
    modelform_factory
)

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course 
        exclude =['Institution','creator','Content','date_added']

class TopicForm(forms.ModelForm):
    class Meta:
        model = Course 
        exclude =[]


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture 
        exclude =[]


class AttachmentsForm(forms.ModelForm):
    class Meta:
        model = attatchment 
        exclude =['Institution','creator','Content','date_added']