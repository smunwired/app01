from django.db import models
import datetime

# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=66)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
    
class Event(models.Model):
    name = models.CharField(max_length=55)
    def __str__(self):
        return self.name

class Activity(models.Model):
    class Type(models.TextChoices):
        Training = "1", "Training"
        Tournament = "2", "Tournament"
        Coaching = "3", "Coaching"
    type = models.CharField(null=True, blank=True,
            max_length = 1,
            choices = Type.choices,
            default = Type.Training)
    activity_date = models.DateField(default=datetime.date.today)
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)
    venue = models.ForeignKey(Venue, null=True, blank=True, on_delete=models.SET_NULL)
    lesson = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    extra = models.TextField(null=True, blank=True)
    def __str__(self):
        return f'{self.event} {self.venue} {self.notes} {self.extra}'
