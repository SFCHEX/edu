from django.shortcuts import render
from django.template import loader
from django.http import Http404
from .models import *

def mainpage(request):
    Courses= Course.objects.order_by('-date_added')
    context = {'Courses': Courses,'attatchment':attatchment,'Topic':Topic,'Lecture':Lecture}
    return render(request, 'mainpage.html', context)







def course(request, course_id):
    try:
        Courses= Course.objects.get(id=course_id)
        context = {'Courses': Courses,'attatchment':attatchment,'Topic':Topic,'Lecture':Lecture}
    except Course.DoesNotExist:
        raise Http404("No Such Course")
    return render(request, 'course.html', context)


