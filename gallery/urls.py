from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns=[
    url('',views.welcome,name = 'welcome'),
    url('about/',views.about,name = 'about'),
    url('search_category/',views.search_images, name='search_images')
    # path("/", .as_view(), name="")('food/',views.school_images,name='food'),
    # path('music/',views.nairobi_images,name='music'),
    # path('hobbies/',views.coast_images,name='hobbies'),
    # path('travel/',views.kericho_images,name='travel'),
    # path('image_details/<int:image_id>',views.image_details,name='image.detail'),
    # # path('search_category/',views.search_images, name='search_images')
    
]