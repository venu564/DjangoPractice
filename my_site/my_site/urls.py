"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.http.response import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request,"index.html")

urlpatterns = [
    path('new_app/',include('new_app.urls')),
    path('my_app/',include('my_app.urls')),
    path('first_app/',include('first_app.urls')),
    path('news_paper/',include('newspaper.urls')),
    path('',home_view,name='home'),
    path('admin/', admin.site.urls),
]

handler404 = 'my_site.views.custom_error_page_view'