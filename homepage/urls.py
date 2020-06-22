
from django.urls import path
from  . import views


urlpatterns = [
    path(r'',views.index,name='index'),
    path(r'home',views.index,name='index'),
    path(r'gallery',views.gallery,name='gallery'),
    path(r'aboutus',views.aboutus,name='aboutus'),
    path(r'contact',views.contact,name='contact'),
    path(r'services',views.services,name='services'),
    path(r'blog',views.blog,name='blog'),


]
