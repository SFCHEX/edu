from django.urls import path

from . import views

urlpatterns = [
    # ex: /courses/
    path('', views.mainpage, name='mainpage'),
    # ex: /courses/5/
    path('/<int:course_id>', views.course, name='course'),
]




