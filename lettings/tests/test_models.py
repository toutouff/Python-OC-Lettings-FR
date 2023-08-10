from django.test import TestCase
from lettings.models import Address, Letting


class AdressesTest(TestCase):
    def create_address(self, number, street, city, state, zip_code, country_iso_code):
        return Address.objects.create(number=number, street=street, city=city, state=state, zip_code=zip_code, country_iso_code=country_iso_code)

    def test_address_str(self):
        address = self.create_address(73,'rue de la paix', 'Paris', 'FR', 75000, 'FR')
        self.assertEqual(str(address), "73 rue de la paix")


class LettingsTest(TestCase):
    def create_letting(self, title, address):
        return Letting.objects.create(title=title, address=address)

    def test_letting_str(self):
        address = Address.objects.create(number=73, street='rue de la paix', city='Paris', state='FR', zip_code=75000, country_iso_code='FR')
        letting = self.create_letting("Letting 1", address)
        self.assertEqual(str(letting), "Letting 1")



