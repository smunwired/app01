from django.db import models

# Create your models here.

class Agency(models.Model):
  name = models.CharField(max_length=155)
  def __str__(self):
    return self.name

class Type(models.Model):
  name = models.CharField(max_length=55)
  def __str__(self):
    return self.name


class Booking(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)
    agency = models.ForeignKey(Agency, on_delete=models.PROTECT, null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    event_date_from = models.DateField(null=True, blank=True)
    event_date_to = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=155)
    purchase_price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
