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

def login(request):
    return render(request, 'ewp/login.html')



def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()
            course_id = form.instance.id
            return redirect('topic-create',course_id) 
    else: 
        form = CourseForm()
    context = {'form':form}
    
    return render(request, 'ewp/create_course.html',context)


def create_topic(request,course_id):
    if request.method == 'POST':
        course = Course.objects.get(id = course_id)
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            topic_id = form.instance.id
            topic = Topic.objects.get(id=topic_id)
            course.Content.add(topic)
            return HttpResponse('<h1>Hi</h1>')
    else:
        form = TopicForm()
    context = {'form': form}
    context['Name']='Topic Name'
    return render(request, 'ewp/create_topic.html', context)









"""
class CourseListView(ListView):
    model = Course
    template_name = 'ewp/archive.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Courses'
    ordering = ['-date_posted']

class CourseCreateView(LoginRequiredMixin,CreateView):
    model = Course
    fields = ['Name','Description','Content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    fields = ['Name','creator','Description','date_added','Content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        course= self.get_object()
        if self.request.user == course.creator:
            return True
        return False


class CourseDeletView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.creator:
            return True
        return False

"""