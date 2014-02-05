from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    url(r'^store_locator/', include('store_locator.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
