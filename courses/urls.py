from django.urls import path

from . import views

app_name = "courses"
urlpatterns = [
    # ex: /courses/
    path('', views.mainpage, name='mainpage'),
    # ex: /courses/5/
    path('<int:course_id>', views.course, name='course'),
]




