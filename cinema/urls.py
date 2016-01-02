"""tgich URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_title/$', views.add_title, name='add_title'),
    url(r'^del_title/$', views.del_title, name='del_title'),
    url(r'^update_title/(?P<id>[\w-]+)$', views.update_title, name='update_title'),
    url(r'^title/$', views.display_title, name='display_title'),

    url(r'^add_artist/$', views.add_artist, name='add_artist'),
]
