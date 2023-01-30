from django.shortcuts import render
from django.template import loader
from django.http import Http404
from .models import Course

def mainpage(request):
    Courses= Course.objects.order_by('-date_added')
    context = {'Courses': Courses}
    return render(request, 'courses/mainpage.html', context)







def course(request, course_id):
    try:
        Courses= Course.objects.get(pk=course_id)
        context = {'Courses': Courses}
    except Course.DoesNotExist:
        raise Http404("No Such Course")
    return render(request, 'courses/course.html', context)


