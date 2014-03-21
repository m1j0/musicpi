from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       #url(r'^titles/', include('title.urls')),
                       url(r'^genre/', include('genre.urls')),
                       #url(r'^playlist/', include('playlist.urls')),
                       #url(r'^player/', include('player.urls')),
                       url(r'^admin/', include(admin.site.urls)))
