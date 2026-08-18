from django.db import models
from bikes.models import Bike
import datetime

# Create your models here.

class Ride(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.PROTECT, default='9')
    dtr = models.DateField(default=datetime.date.today())
    tm = models.TimeField(null=True)
    dst = models.FloatField(null=True)
    av = models.FloatField(null=True)
    mx = models.FloatField(null=True)
    odo = models.IntegerField(null=True)
    route = models.TextField(null=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "date %s time %s" % (self.dtr.strftime('%d-%m-%Y'), self.tm.strftime('%H:%M'))

class Point(models.Model):
    short_name = models.CharField(max_length=10)
    long_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.long_name}"
    
class RidePoint(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.PROTECT)
    point = models.ForeignKey(Point, on_delete=models.PROTECT)
    tm = models.TimeField(null=True)
    dst = models.FloatField(null=True)
    av = models.FloatField(null=True)
    max = models.FloatField(null=True)
    odo = models.IntegerField(null=True)
