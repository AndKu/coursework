from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from gallery.views import *
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'gallery.views.upload_image'),
    url(r'^gallery/$', ImageList.as_view()),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    # Examples:
    # url(r'^$', 'coursework.views.home', name='home'),
    # url(r'^coursework/', include('coursework.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
