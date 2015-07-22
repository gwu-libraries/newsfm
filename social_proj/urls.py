"""social_proj URL Configuration

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
from social_app.views import UserListView, GroupListView, CollectionListView
from social_app.views import SeedListView, SeedSetListView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'social_app.views.login'),
    # url(r'^home/$', 'social_app.views.home'),
    url(r'^logout/$', 'social_app.views.logout'),
    # url(r'^gwlogin/$', 'social_app.views.gwlogin'),
    # url(r'^profile/$', 'social_app.views.profile'),
    # url(r'^gwhome/$', 'social_app.views.gwhome'),
    url(r'^homeview/$', 'social_app.views.homeview'),
    url(r'^collection/$', 'social_app.views.collection'),
    url(r'^group/$', 'social_app.views.group'),
    url(r'^collectionedit/$', 'social_app.views.collectionedit'),
    url(r'^groupedit/$', 'social_app.views.groupedit'),
    url(r'^seedset/$', 'social_app.views.seedset'),
    url(r'^seedsetedit/$', 'social_app.views.seedsetedit'),
    url(r'^seed/$', 'social_app.views.seed'),
    url(r'^seededit/$', 'social_app.views.seededit'),
    url(r'^user/$', 'social_app.views.user'),
    url(r'^useredit/$', 'social_app.views.useredit'),
    url(r'^users/$', UserListView.as_view(), name='users'),
    url(r'^collections/$', CollectionListView.as_view(), name='collections'),
    url(r'^groups/$', GroupListView.as_view(), name='groups'),
    url(r'^seeds/$', SeedListView.as_view(), name='seeds'),
    url(r'^seedsets/$', SeedSetListView.as_view(), name='seedsets'),
    url(r'^complete/(?P<backend>[^/]+)/$', 'social_app.views.complete',
        name='complete'),
]
