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
    event_name = models.CharField(max_length=155,null=True,blank=True)
    reference = models.CharField(max_length=55,null=True,blank=True)
    notes = models.CharField(max_length=455,null=True,blank=True)
    purchase_price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.reference}"

class Destination(models.Model):
    name = models.CharField(max_length=55)
    code = models.CharField(max_length=5, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.name

class Flight(models.Model):
    flight_no = models.CharField(max_length=55, null=True, blank=True)
    depart_dest_id = models.ForeignKey(Destination, related_name='depart_dest_id', on_delete=models.PROTECT, null=True, blank=True)
    departure_time = models.TimeField(null=True, blank=True)
    arrive_dest_id = models.ForeignKey(Destination, related_name='arrive_dest_id', on_delete=models.PROTECT, null=True, blank=True)
    arrival_time = models.TimeField(null=True, blank=True)
    operator_id = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.flight_no}"

class Stage(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.PROTECT, null=True, blank=True)
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT, null=True, blank=True)
    seats = models.IntegerField(null=True, blank=True)
    sequence = models.IntegerField(null=True, blank=True)
    stage_date = models.DateField(null=True, blank=True)

  
