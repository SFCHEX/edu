from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.index, name='ewp-about'),
    path('', views.home, name='ewp-home'),
    path('login/',views.login,name = 'ewp-login'),
    path('archive',views.archive,name = 'ewp-archive')
]
