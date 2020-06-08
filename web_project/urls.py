"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
from django.conf.urls import url
from django.urls import re_path, path
from web_project.views import hello,runoob,main,kong
from django.contrib.staticfiles.views import serve
from django.contrib import admin
from . import testdb
from . import search

#urlpatterns = [re_path(r'', index, name='index')]
urlpatterns = [
    path('hello/', hello),
    path('runoob/', runoob),
    path('testdb/', testdb.testdb),
    path('search-form/', search.search_form),
    path('search/', search.search),
    path('search-post/', search.search_post),
    path('man/', main),
    path('favicon.ico', serve, {'path': 'images/favicon.ico'}),
    path('', kong),
    url(r'^admin/', admin.site.urls)
]