from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.index, name='ewp-about'),
    path('', views.home, name='ewp-home'),


    path('course/new',views.create_course, name='course-create'), #put in the course app

    path('course/new/<int:course_id>/',views.create_topic,name='create-topic'),

#   htmx views for topics
    path('courses/topic/form/',views.create_topic_form, name='topic-form'),
    path('courses/topic/<int:pk>/',views.detail_topic, name='topic-detail'),
    path('courses/topic/<int:pk>/delete/',views.delete_topic, name='topic-delete'),
    path('courses/topic/<int:pk>/update/',views.update_topic, name='topic-update'),

]
