from django.core.urlresolvers import reverse
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

        self.assertEqual(l.__unicode__(
        ), "{0} :: {1}, {2}".format(l.name, l.city, l.state))


class LocationTestBase(TestCase):
    def setUp(self):
        self.l_1 = Location.objects.create(name='Location 1',
                                           address='addr',
                                           address_2='addr2',
                                           city='city 4',
                                           state='AR',
                                           zip_code='90210',
                                           location=SAMPLE_POINT_1,
                                           description='lorem ipsum')
        self.l_2 = Location.objects.create(name='Location 2',
                                           address='addr',
                                           address_2='addr2',
                                           city='city 2',
                                           state='AR',
                                           zip_code='90210',
                                           location=SAMPLE_POINT_2,
                                           description='lorem ipsum')
        self.l_3 = Location.objects.create(name='Location 4',
                                           address='addr',
                                           address_2='addr2',
                                           city='city 3',
                                           state='AR',
                                           zip_code='90210',
                                           location=SAMPLE_POINT_3,
                                           description='lorem ipsum')
        self.l_4 = Location.objects.create(name='Location 4',
                                           address='addr',
                                           address_2='addr2',
                                           city='city 1',
                                           state='AR',
                                           zip_code='90210',
                                           location=SAMPLE_POINT_4,
                                           description='lorem ipsum')


class LocationViewTest(LocationTestBase):
    def test_location_by_state_view(self):
        response = self.client.get(reverse('store_locator_locations_by_state',
                                           kwargs={'state': 'AR'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_locator/location_list.html')
        self.assertQuerysetEqual(response.context['location_list'],
                                 [repr(self.l_4), repr(self.l_2), repr(self.l_3), repr(self.l_1)])

    def test_location_by_state_view_unknown_state(self):
        response = self.client.get(reverse('store_locator_locations_by_state',
                                           kwargs={'state': 'BLAH'}))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['location_list'],
                                      Location.objects.none())

    def test_location_detail_view(self):
        response = self.client.get(self.l_1.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_locator/location_detail.html')
        self.assertEqual(response.context['location'], self.l_1)

class LocationRadiusSearchTest(LocationTestBase):
    def test_radius_search(self):
        search_point = '34.74759,-92.271053'
        search_distance = '5'
        response = self.client.get(reverse('store_location_find_by_point'),
                                   {'location':search_point,
                                    'distance':search_distance})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_locator/location_search.html')
        self.assertEqual(response.context['distance'], int(search_distance))
        self.assertEqual(response.context['search_spot'], search_point)
        self.assertQuerysetEqual(response.context['location_list'],
                                 [repr(self.l_1), repr(self.l_2), repr(self.l_3)])


    def test_radius_search_invalid_distance(self):
        search_point = '34.74759,-92.271053'
        response = self.client.get(reverse('store_location_find_by_point'),
                                   {'location':search_point,
                                    'distance':'-2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['distance'], 20)

        response = self.client.get(reverse('store_location_find_by_point'),
                                   {'location':search_point,
                                    'distance':'0'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['distance'], 20)

        response = self.client.get(reverse('store_location_find_by_point'),
                                   {'location':search_point,
                                    'distance':'101'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['distance'], 20)

        response = self.client.get(reverse('store_location_find_by_point'),
                                   {'location':search_point})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['distance'], 20)

        response = self.client.get(reverse('store_location_find_by_point'),
                                   {'location':search_point,
                                    'distance':'asdfadfadsf'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['distance'], 20)



