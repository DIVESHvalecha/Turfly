from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('accounts/', include('allauth.urls')),
]