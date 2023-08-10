from django.contrib import admin
from django.urls import path, include
import django.conf.urls as error

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('admin/', admin.site.urls),
]

error.handler404 = views.error_404
error.handler500 = views.error_500
