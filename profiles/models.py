from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """Profile model
    :param models.Model: Django model
    :type models.Model: class
    :field user: user
    :type user: User
    :field favorite_city: favorite city
    :type favorite_city: str
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """String representation of the profile object
        :return: string representation of the profile object
        :rtype: str
        """
        return self.user.username
