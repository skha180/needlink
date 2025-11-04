# core/urls/web_urls.py
from django.urls import path
from core.viewss.web_views import home

urlpatterns = [
    path("", home, name="core_home"),
]
