from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'ewp/about.html')


def home(request):
    return render(request, 'ewp/home.html')

def login(request):
    return render(request, 'ewp/login.html')

