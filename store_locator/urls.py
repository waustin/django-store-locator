from django.conf.urls import patterns, include, url

from .views import LocationsByState, LocationDetail, LocationRadiusSearch, LocationsByZipCode

urlpatterns = patterns('',
    # Find locations near requires a GET parmeter of location and distance in miles
    url(r'^find/$',
        LocationRadiusSearch.as_view(),
        name='store_location_find_by_point'),

    url(r'^find/zip/$',
        LocationsByZipCode.as_view(),
        name='store_location_find_by_zip'),

    # List locations by state
    url(r'^state/(?P<state>[-\w]+)/$',
        LocationsByState.as_view(),
        name='store_locator_locations_by_state'),

    # Location Lookup
    url(r'^location/(?P<pk>\d+)/',
        LocationDetail.as_view(),
        name='store_locator_location_detail'),
)
