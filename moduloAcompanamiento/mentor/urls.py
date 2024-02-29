from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.mentores_view, name='mentores_view'),
    path('<int:pk>', views.mentor_view, name='mentor_view'),
]
