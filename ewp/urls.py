from django.urls import path
from .views import(
 CourseListView,
 CourseCreateView,
 CourseUpdateView,
 CourseDeletView
)    
from . import views

urlpatterns = [
    path('about/', views.index, name='ewp-about'),
    path('', views.home, name='ewp-home'),
    path('login/',views.login,name = 'ewp-login'),
    path('archive',CourseListView.as_view(),name = 'ewp-archive'),
    path('course/new',CourseCreateView.as_view(), name='course-create'), #put in the course app
    path('course/<int:pk>/update/',CourseUpdateView.as_view(),name='course-update'),
    path('course/<int:pk>/delete/',CourseDeletView.as_view(),name='course-delete')

]
