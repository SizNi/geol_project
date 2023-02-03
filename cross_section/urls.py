from django.contrib import admin
from django.urls import path
from cross_section import views


urlpatterns = [
    path('', views.CrossIndexView.as_view(), name='home_cross'),
]
