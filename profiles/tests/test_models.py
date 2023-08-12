from django.contrib.auth.models import User
from django.test import TestCase
from profiles.models import Profile


class Test(TestCase):
    def create_profiles(self, user, favorite_city):
        return Profile.objects.create(user=user, favorite_city=favorite_city)

    def test_profile_str(self):
        user = User.objects.create_user(username='Test_user', password='12345')
        profile = self.create_profiles(user=user, favorite_city='Paris')
        self.assertEqual(str(profile), profile.user.username)
