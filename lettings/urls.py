from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('lettings/', views.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
]
