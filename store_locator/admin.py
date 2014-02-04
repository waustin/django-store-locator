from django.contrib import admin
from django.contrib.gis import admin as geoadmin

from .models import ZipCodeLocation, Location

class ZipCodeLocationAdmin(geoadmin.OSMGeoAdmin):
    default_lat = 4097417.875510718
    default_lon = -10358729.462251822
    default_zoom = 4
    map_width = 850
    map_height = 700
    list_display = ('zip_code',)
    search_fields = ('zip_code',)


class LocationAdmin(geoadmin.OSMGeoAdmin):
    default_lat = 4097417.875510718
    default_lon = -10358729.462251822
    default_zoom = 4
    map_width = 850
    map_height = 700

    list_display = ('name', 'display_address', 'state', 'zip_code')
    list_filter = ('state',)
    search_fields = ('name', 'address', 'city', 'state', 'zip_code')


admin.site.register(ZipCodeLocation, ZipCodeLocationAdmin)
admin.site.register(Location, LocationAdmin)
