from django.shortcuts import render
from django.http import Http404
from .models import Course

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def mainpage(request):
    Courses= Course.objects.order_by('-date_added')
    context = {'Courses': Courses}
    return render(request, 'mainpage.html', context)

def course(request, course_id):
    try:
        Sel_Course= Course.objects.get(id=course_id)
        context = {'Course': Sel_Course}
    except Course.DoesNotExist:
        raise Http404("No Such Course")
    return render(request, 'course.html', context)


class CourseListView(ListView):
    model = Course
    template_name = 'ewp/archive.html'  # <app>/<model>_<viewtype>.html
    ordering = ['-date_posted']
    context_object_name = 'Courses'


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        course = self.get_object()
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
