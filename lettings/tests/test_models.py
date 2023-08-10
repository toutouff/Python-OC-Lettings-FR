from django.test import TestCase
from lettings.models import Address, Letting


def create_address(number, street, city, state, zip_code, country_iso_code):
    return Address.objects.create(number=number, street=street, city=city,
                                  state=state, zip_code=zip_code,
                                  country_iso_code=country_iso_code)


class AdressesTest(TestCase):

    def test_address_str(self):
        address = create_address(73, 'rue de la paix', 'Paris',
                                 'FR', 75000, 'FR')
        self.assertEqual(str(address), "73 rue de la paix")


def create_letting(title, address):
    return Letting.objects.create(title=title, address=address)


class LettingsTest(TestCase):

    def test_letting_str(self):
        address = Address.objects.create(number=73, street='rue de la paix',
                                         city='Paris', state='FR',
                                         zip_code=75000, country_iso_code='FR')
        letting = create_letting("Letting 1", address)
        self.assertEqual(str(letting), "Letting 1")
