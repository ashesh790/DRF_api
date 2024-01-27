from .views import * 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index),
    path('add', post_data),
    path('update_put/<id>', update_put_data), 
    path('update_patch_data/<id>', update_patch_data),
    path('delete/<id>', delete_data_record), 
    path('book_data/', book_data),
    path('register_user', register_user.as_view())
]