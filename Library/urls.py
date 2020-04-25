from django.contrib import admin
from django.urls import path

from Library import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('admin/<int:id>/index', views.admin_index, name='admin_index'),
    path('user/index', views.user_index, name='user_index'),
    path('admin/<int:id>/booklist', views.admin_booklist, name='admin_booklist'),
    path('admin/<int:id>/search', views.admin_search, name='admin_search'),
]
