from django.test import TestCase

# Create your tests here

class SimpleTest(TestCase):

    def test_basic_addition(self):
        """ Test  1 + 1 equals 2 """
        self.assertEqual(1 + 1, 2)
