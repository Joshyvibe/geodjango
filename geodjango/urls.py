
from django.contrib import admin
from django.urls import path
from geo_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_location/', views.submit_location, name='submit_location'),
    path('admin/', admin.site.urls),
]
