from django.shortcuts import render
from django.template import loader
from django.http import Http404
from .models import Course

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


def topic(request, topic_id):
    try:
        Sel_Course= Topic.objects.get(id=topic_id)
        context = {'Course': Sel_Course}
    except Course.DoesNotExist:
        raise Http404("No Such Course")
    return render(request, 'course.html', context)



