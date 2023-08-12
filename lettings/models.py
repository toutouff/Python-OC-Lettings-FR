from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


# Create your models here.


class Address(models.Model):
    """Address model
    :param models.Model: Django model
    :type models.Model: class
    :field number: number
    :type number: int
    :field street: street
    :type street: str
    :field city: city
    :type city: str
    :field state: state
    :type state: str
    :field zip_code: zip code
    :type zip_code: int
    :field country_iso_code: country ISO code
    :type country_iso_code: str
    """

    class Meta:
        verbose_name_plural = 'Addresses'

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """String representation of the address
        :return: string representation of the address
        :rtype: str
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Letting model
    :param models.Model: Django model
    :type models.Model: class
    :field title: title
    :type title: str
    :field address: address
    :type address: Address

    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the letting object
        :return: string representation of the letting object
        :rtype: str
        """
        return self.title
