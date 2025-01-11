from django.test import TestCase
from egyptianidapp.factories import NationalIDFactory

class NationalIDTestCase(TestCase):
    def setUp(self):
        self.national_id = NationalIDFactory(number='29901011501234')

    def test_national_id_creation(self):
        self.assertIsNotNone(self.national_id.number)
        self.assertTrue(len(self.national_id.number) == 14)
        self.assertIsNotNone(self.national_id.birth_date)
        self.assertIsNotNone(self.national_id.location)
