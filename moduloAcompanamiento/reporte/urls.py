from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reportes_view, name='reportes_view'),
    path('<int:pk>', views.reporte_view, name='reporte_view'),
]