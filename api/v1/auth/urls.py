from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'api_v1_authentication'

urlpatterns = [
    path('', views.index),
    path('verify-code/', views.verify_code),
]
