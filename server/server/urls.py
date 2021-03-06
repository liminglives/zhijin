"""server URL Configuration

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

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.test),
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^get_news/', views.get_news),
    url(r'^get_news_detail/', views.get_news_detail),
    url(r'^get_topic/', views.get_topic),
    url(r'^topiclist/', views.topiclist),
    url(r'^topicdetail/', views.get_topic_detail),
    #url(r'^get_topic_detail/', views.get_topic_detail),
    url(r'^create_topic/', views.create_topic),
    url(r'^topicvote/', views.topic_vote),
]
