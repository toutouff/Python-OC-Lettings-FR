from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile
from pprint import pprint


class Test(TestCase):
    def setUp(self):
        user = User.objects.create_user('test_user',password='test_password')
        profile = Profile.objects.create(user=user,favorite_city='test_city')

    def test_index(self,):
        url = reverse('profiles_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('test_user', response.content.decode())

    def test_profile(self):
        url = reverse('profile', kwargs={'username': 'test_user'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('test_user', response.content.decode())
        self.assertIn('test_city', response.content.decode())

    def test_profile_not_found(self):
        url = reverse('profile', kwargs={'username': 'test_user2'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertIn('Error : Profile not found', response.content.decode())
