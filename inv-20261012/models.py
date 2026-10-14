from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=55)
    def __str__(self):
        return f"{self.name}"

class Manufacturer(models.Model):
    name = models.CharField(max_length=35, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.name}{self.country}"

class Brand(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.name}"


from django.core.validators import MinValueValidator, MaxValueValidator
class Instrument(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True, blank=True)
    model = models.CharField(max_length=35)
    year_of_manufacture = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1000), MaxValueValidator(3000)])
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    purchase_price = models.FloatField(null=True, blank=True)
    sold_date = models.DateField(null=True, blank=True)
    sold_price = models.FloatField(null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model}"
#        return {self.badge, self.model}

