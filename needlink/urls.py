"""
URL configuration for needlink project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core (Auth, Profile, etc.)
    path('api/v1/core/', include('core.urls.api_urls')),
    path('', include('core.urls.web_urls')),

    # Services (Requests, Providers, Categories)
    path('api/v1/services/', include('services.urls.api_urls')),
    path('services/', include('services.urls.web_urls')),
]
