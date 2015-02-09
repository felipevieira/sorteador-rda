from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from sorteador.views import *

import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sorteador.views.home', name='home'),
    url(r'^new/', 'sorteador.views.new'),
    url(r'^sortear/', 'sorteador.views.sortear'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT }),
)
