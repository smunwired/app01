from django.contrib import admin

# Register your models here.

from .models import Venue, Event, Activity

admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Activity)

