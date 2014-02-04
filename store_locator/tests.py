from django.test import TestCase

from .models import ZipCodeLocation, Location


SAMPLE_POINT_1 = 'POINT(-92.289595 34.746481)'
SAMPLE_POINT_2 = 'POINT(-92.273494 34.744487)'
SAMPLE_POINT_3 = 'POINT(-92.489047 34.810632)'
SAMPLE_POINT_4 = 'POINT(-94.251795 35.7813)'
SAMPLE_POINT_5 = 'POINT(-93.053321 34.516402)'


class ModelTestCase(TestCase):
    def test_can_create_zip_loctation(self):
        z = ZipCodeLocation.objects.create(zip_code='72201',
                                           location=SAMPLE_POINT_1)

        self.assertEqual(z.__unicode__(), z.zip_code)

    def test_can_create_location(self):
        l = Location.objects.create(name='Location 1',
                                    address='addr',
                                    address_2='addr2',
                                    city='city',
                                    state='AR',
                                    zip_code='90210',
                                    location=SAMPLE_POINT_2,
                                    description='lorem ipsum')

        self.assertEqual(l.__unicode__(), "{0} :: {1}, {2}".format(l.name, l.city, l.state))
