"""Blacklearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    url(r'login', views.login),
    url(r'register', views.resgister),
    url(r'ucenter', views.user_center),
    url(r'forget', views.user_forget),
    url(r'logout', views.logout),
    url(r'pay', views.payvip),
    url(r'info', views.user_info),
    url(r'usermodify',views.uinfo_modify),
]
