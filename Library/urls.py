from django.contrib import admin
from django.urls import path

from Library import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('admin/index', views.admin_index, name='admin_index'),
    path('user/index', views.user_index, name='user_index'),
]
