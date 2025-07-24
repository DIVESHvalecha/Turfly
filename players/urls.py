from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_home, name='player_home'),
    path('turf/<int:turf_id>/', views.turf_detail, name='turf_detail'),
] 