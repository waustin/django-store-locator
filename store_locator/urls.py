from django.conf.urls import patterns, include, url

from .views import LocationsByState, LocationDetail

urlpatterns = patterns('',
    # List locations by state
    url(r'^state/(?P<state>[-\w]+)/$',
        LocationsByState.as_view(),
        name='store_locator_locations_by_state'),

    url(r'^location/(?P<pk>\d+)/',
        LocationDetail.as_view(),
        name='store_locator_location_detail'),
)
