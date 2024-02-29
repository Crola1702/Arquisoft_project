from django.contrib import admin 
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.universidades_view, name = 'universidades_view'),
    path('<slug:pk>', views.universidad_view, name = 'universidad_view'),
]