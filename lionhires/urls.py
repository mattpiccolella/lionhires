from django.contrib import admin
from django.conf.urls import patterns, include, url


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'lionhires.apps.jobs.views.home', name='home'),
    url(r'^profile/', 'lionhires.apps.jobs.views.profile', name='profile'),
    url(r'^logout/', 'lionhires.apps.jobs.views.logout', name='logout')
)
