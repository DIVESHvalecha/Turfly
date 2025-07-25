"""
URL configuration for turf_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usrs.views import landing


urlpatterns = [
    path('', landing, name='landing'),
    path('admin/', admin.site.urls),
    path('usrs/', include(('usrs.urls', 'usrs'), namespace='usrs')),
    path('owner/', include(('owner.urls', 'owner'), namespace='owner')),  # <-- Add namespace here
    path('accounts/', include('allauth.urls')),
    path('players/', include(('players.urls', 'players'), namespace='players')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
