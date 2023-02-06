from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.index, name='ewp-about'),
    path('', views.home, name='ewp-home'),
    path('login/',views.login,name = 'ewp-login'),
    path('course/new',views.create_course, name='course-create'), #put in the course app
    path('course/new/<int:course_id>',views.create_topic,name='topic-create'),
    #path('course/<int:pk>/update/',CourseUpdateView.as_view(),name='course-update'),
    #path('course/<int:pk>/delete/',CourseDeletView.as_view(),name='course-delete')

]
