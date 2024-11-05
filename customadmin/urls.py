from django.contrib import admin
from django.urls import path
from customadmin import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signusers/', views.signusers, name='signusers'),
    path('userpatient/', views.userpatient, name='userpatient'),
    path('userdonor/', views.userdonor, name='userdonor'),
    path('dashboard_view/', views.dashboard_view, name='dashboard_view'),



]
