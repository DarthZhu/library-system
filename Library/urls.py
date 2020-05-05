from django.contrib import admin
from django.urls import path

from Library import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('admin/<int:id>/index', views.admin_index, name='admin_index'),
    path('admin/<int:id>/search', views.admin_search, name='admin_search'),
    path('admin/<int:id>/add', views.admin_add, name='admin_add'),
    path('admin/<int:id>/edit', views.admin_edit, name='admin_edit'),
    path('admin/<int:id>/bills', views.admin_bill, name='admin_bill'),
    path('admin/<int:id>/pay', views.admin_pay, name='admin_pay'),
    path('admin/<int:id>/confirm', views.admin_confirm, name='admin_confirm'),
    path('admin/<int:id>/cancel', views.admin_cancel, name='admin_cancel'),
    path('admin/<int:id>/check', views.admin_check, name='admin_check'),
    path('user/<int:id>/index', views.user_index, name='user_index'),
    path('user/<int:id>/search', views.user_search, name='user_search'),
    path('user/<int:id>/bills', views.user_bill, name='user_bill'),
    path('user/<int:id>/buy', views.user_buy, name='user_buy'),
    path('user/<int:id>/pay', views.user_pay, name='user_pay'),
    path('user/<int:id>/confirm', views.user_confirm, name='user_confirm'),
    path('user/<int:id>/cancel', views.user_cancel, name='user_cancel'),
    path('user/<int:id>/edit', views.user_edit, name='user_edit'),
]
