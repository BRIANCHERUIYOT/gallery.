from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns=[
    url('',views.welcome,name = 'welcome'),
    url('about/',views.about,name = 'about'),
    path('search_category/',views.search_images, name='search_images')
    
]