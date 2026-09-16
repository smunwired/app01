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
        Club = "4", "Club"
    type = models.CharField(null=True, blank=True,
            max_length = 1,
            choices = Type.choices,
            default = Type.Club)
    activity_date = models.DateField(default=datetime.date.today)
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)
    venue = models.ForeignKey(Venue, null=True, blank=True, on_delete=models.SET_NULL, default=50)
    lesson = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    extra = models.TextField(null=True, blank=True)
    def __str__(self):
        if (self.event):
            return f'{self.get_type_display()}, {self.activity_date}, {self.event}, {self.venue}'
        else:
            return f'{self.get_type_display()}, {self.activity_date}, {self.venue}'
