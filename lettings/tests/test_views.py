from django.test import TestCase
from django.urls import reverse
from lettings.models import Address, Letting

class Test(TestCase):
    def setUp(self):
        data = {
            'address' : {
            'number': 73,
            'street': 'rue de la paix',
            'city': 'Paris',
            'state': 'France',
            'zip_code': 75000,
            'country_iso_code': 'FR'
            },
            'letting':{
            'title': 'Letting 1',
            }
        }
        address = Address.objects.create(**data['address'])
        Letting.objects.create(title=data['letting']['title'], address=address)

    def test_index(self):
        url = reverse('lettings_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Letting 1', response.content.decode())

    def test_letting(self):
        url = reverse('letting', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Letting 1', response.content.decode())
        self.assertIn('73 rue de la paix', response.content.decode())

    def test_letting_not_found(self):
        url = reverse('letting', args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertIn('Error : Letting not found', response.content.decode())

