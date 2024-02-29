from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.estudiantes_view, name='estudiantes_view'),
    path('<int:pk>', views.estudiante_view, name='estudiante_view'),
]
