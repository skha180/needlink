# core/views/web_views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # simple placeholder home page; later replace with template render()
    return HttpResponse("<h1>NeedLink Home (Web)</h1><p>Web views are working.</p>")
