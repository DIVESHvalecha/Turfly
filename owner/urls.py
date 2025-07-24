from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='owner_dashboard'),
    path('add-turf/', views.add_turf, name='add_turf'),
] 