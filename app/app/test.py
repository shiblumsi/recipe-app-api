from django.test import SimpleTestCase
from . import cal

class CalTestCase(SimpleTestCase):
    def test_simhhfhfhfhple(self):
        res = cal.add(13,12)
        self.assertEqual(res,25)