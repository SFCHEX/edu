from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

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


class CourseListView(ListView):
    model = Course
    template_name = 'ewp/archive.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Courses'
    ordering = ['-date_posted']

class CourseCreateView(LoginRequiredMixin,CreateView):
    model = Course
    fields = ['Name','creator','Description','date_added','Content']

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
