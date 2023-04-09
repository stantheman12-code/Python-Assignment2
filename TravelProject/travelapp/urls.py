from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('travel/', views.travel, name='travel'),
    path('bookings/', views.app, name='app'),
]