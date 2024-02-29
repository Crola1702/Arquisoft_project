from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.historialesAcademicos_view, name='historialesAcademicos_view'),
    path('<int:pk>', views.historialAcademico_view, name='historialAcademico_view'),
]