from django.contrib.gis.geos import Point
from django.views.generic import ListView, DetailView

from .models import Location

GOOGLE_MAPS_PROJECTION = 900913
METER_PER_MILE_BUFFER = 2172.334


class LocationRadiusSearch(ListView):
    template_name = 'store_locator/location_search.html'

    def radius_search(self, qs, search_point, search_radius):
        # Create polygon centered at the search point for the give radius
        # search radius is given in miles
        # Return a list of places in that search area
        search_polygon = search_point.buffer(search_radius * METER_PER_MILE_BUFFER)
        return qs.filter(location__within=search_polygon).distance(search_point).order_by('distance')

    def get_search_point(self, longitude, latitude):
        """ return a gis point based on lat long coords (in float) """
        search_point = Point(longitude, latitude, srid=4326)
        search_point.transform(GOOGLE_MAPS_PROJECTION)
        return search_point

    def parse_lat_long(self):
        location = self.request.GET.get('location', None)
        if location is None:
            return None

        location = location.split(',')
        if len(location) != 2:
            return None

        try:
            location = map(float, location)
        except ValueError:
            return None
        return location

    def parse_distance(self):
        distance = self.request.GET.get('distance', 20)
        try:
            distance = int(distance)
        except ValueError:
            distance = 20

        if distance <= 0 or distance > 100:
            distance = 20

        return distance

    def get_queryset(self):
        self.search_spot = None
        self.distance = self.parse_distance()
        location = self.parse_lat_long()
        if location is None:
            return Location.objects.none()

        self.search_spot = ",".join(map(str, location))

        search_point = self.get_search_point(location[1], location[0])
        location_qs = Location.objects.all()
        return self.radius_search(location_qs, search_point, self.distance)

    def get_context_data(self, **kwargs):
        context = super(LocationRadiusSearch, self).get_context_data(**kwargs)
        context['distance'] = self.distance
        context['search_spot'] = self.search_spot
        return context


class LocationsByState(ListView):
    def get_queryset(self):
        self.state = self.kwargs.get('state', None)
        if self.state is None:
            return Location.objects.none()
        else:
            return Location.objects.filter(state=self.state).order_by('city')

    def get_context_data(self, **kwargs):
        context = super(LocationsByState, self).get_context_data(**kwargs)
        context['state'] = self.state
        return context


class LocationDetail(DetailView):
    model = Location
