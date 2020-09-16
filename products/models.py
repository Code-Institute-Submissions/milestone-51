from django.db import models


class Continent(models.Model):

    class Meta:
        verbose_name_plural = 'Continents'

    name = models.CharField(max_length=100)
    readable_name = models.CharField(max_length=250, null=True, blank=True)

    def get_readable_name(self):
        return self.readable_name

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    readable_name = models.CharField(max_length=250, null=True, blank=True)

    def get_readable_name(self):
        return self.readable_name

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    continent = models.ForeignKey('Continent', null=True,
                                  blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    nation_of_origin = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
