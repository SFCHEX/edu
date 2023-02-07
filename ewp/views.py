from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from courses.models import Course
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


def index(request):
    return render(request,'ewp/about.html')


def home(request):
    return render(request, 'ewp/home.html')




def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()
            course_id = form.instance.id
            return redirect('create-topic',course_id) 
    else: 
        form = CourseForm()
    context = {'form':form}
    
    return render(request, 'ewp/create_course.html',context)


def create_topic(request,course_id):
    course = Course.objects.get(id=course_id)
    topics = course.Content.all
    if request.method == 'POST':
        
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save()
            course.Content.add(topic)
            return redirect('topic-detail',topic.pk)
        else:
            context = {'form': TopicForm()}
            return render(request, 'partials/topic_form.html', context)

    context = {'form': TopicForm(),
               'topics': topics
               }
    return render(request, 'ewp/create_topic.html', context)


def create_topic_form(request):
    context = {
        'form':TopicForm()
    }
    return render(request,'partials/topic_form.html',context)



def detail_topic(request,pk):
    topic =Topic.objects.get(pk=pk)
    context = {
        'topic': topic
    }
    return render(request,'partials/topic_detail.html',context)


def delete_topic(request, pk):
    topic = Topic.objects.get(pk=pk)
    topic.delete()
    return HttpResponse('')


def update_topic(request,pk):
    topic = Topic.objects.get(pk=pk)
    form = TopicForm(request.POST or None ,instance=topic)
    if request.method == 'POST':
        if form.is_valid():
            topic = form.save()
            return redirect('topic-detail', topic.pk)
    context = {
        'form': form,
        'topic':topic
    }
    return render(request, 'partials/topic_form.html', context)
