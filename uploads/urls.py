from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),
]
