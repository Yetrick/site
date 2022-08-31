from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name=''),
    path('blog', views.blog, name='blog'),
    path('photo', views.photo, name='photo'),
    path('news', views.news, name='news')
]