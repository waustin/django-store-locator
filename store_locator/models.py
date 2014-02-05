from django.contrib.gis.db import models


class ZipCodeLocation(models.Model):
    zip_code = models.CharField(max_length=7, db_index=True, unique=True)
    location = models.PointField(srid=4326)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.zip_code


class Location(models.Model):
    """ Store Location """
    name = models.CharField(max_length=125, db_index=True)

    address = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, db_index=True)
    state = models.CharField(max_length=10, db_index=True)
    zip_code = models.CharField(max_length=5, db_index=True)

    location = models.PointField(srid=4326, null=True, blank=True)

    description = models.TextField(blank=True)

    objects = models.GeoManager()

    def display_address(self):
        return "{0} {1} {2}, {3} {4}".format(self.address, self.address_2,
                                             self.city, self.state, self.zip_code)

    def __unicode__(self):
        return "{0} :: {1}, {2}".format(self.name, self.city, self.state)

    @models.permalink
    def get_absolute_url(self):
        return ('store_locator_location_detail', (), {'pk':self.id})

    class Meta:
        ordering = ('name',)
