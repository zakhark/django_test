"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from hello.views import hello
from hello.views import abascript
from hello.views import hours_ahead
from blat import views
#from dashboard import views as dviews

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^abascript/$', abascript),
    url(r'^time/$', hello),
    url(r'^time/plus/(\d+)/$', hours_ahead),
#    url(r'^$', views.home, name="homepage"),
    url(r'^$', views.IndexView.as_view(), name="homepage"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'login/$', auth_views.login, name="login"),
    url(r'logout/$', auth_views.logout, name="logout"),
    url(r'my/$', views.MyView.as_view(), name="myview"),
#    url(r'^dash/$', dviews.IndexView.as_view(), name="homepage"),
]
