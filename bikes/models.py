from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    badge = models.CharField(max_length=35)
    manufacturer = models.CharField(max_length=35, null=True, blank=True)

    def __str__(self):
        return f"{self.badge}"

from django.core.validators import MinValueValidator, MaxValueValidator
class Bike(models.Model):
    badge = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    model = models.CharField(max_length=35)
    year_of_manufacture = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1000), MaxValueValidator(3000)])
    purchase_date = models.DateField(null=True, blank=True)
    purchase_price = models.FloatField(null=True, blank=True)
    sold_date = models.DateField(null=True, blank=True)
    sold_price = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.badge} {self.model}"
#        return {self.badge, self.model}
