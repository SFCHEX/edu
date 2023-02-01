from django.urls import path

from . import views
from .views import (
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeletView
)


urlpatterns = [
    # ex: /courses/
    path('', views.mainpage, name='mainpage'),
    # ex: /courses/5/
    path('<int:pk>', views.course, name='course'),
    path('archive/', CourseListView.as_view(), name='course-archive'),
    path('course/new', CourseCreateView.as_view(),name='course-create'),  # put in the course app
    path('course/<int:pk>/update/',CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/delete/', CourseDeletView.as_view(), name='course-delete')
]




