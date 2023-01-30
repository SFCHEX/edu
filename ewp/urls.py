from django.urls import path,include

from . import views

app_name='ewp'
urlpatterns = [
    path('about/', views.index, name='ewp-about'),
    path('', views.home, name='ewp-home'),
    path('login/',views.login,name = 'ewp-login'),
    path('courses/',include('courses.urls'),name = 'ewp-courses'),
]
