"""gafferon_games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^category/(?P<category_id>\d+)$', by_category, name='list_by_category'),
    url(r'^tag/(?P<tag_id>\d+)$', by_tag, name='list_by_tag'),
    url(r'^article/(?P<article_id>\d+)$', article_detail, name='article_detail'),
    url(r'^about$', about, name='about'),
    url(r'^$', index, name='index'),
]
