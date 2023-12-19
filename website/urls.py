from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('/news', views.news, name='news'),
    path('/announcements', views.announcements, name='announcements'),
    # Add more paths as needed
]