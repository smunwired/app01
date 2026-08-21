from django.contrib import admin

from .models import Country, Manufacturer, Instrument, Brand

admin.site.register(Country)
admin.site.register(Manufacturer)
admin.site.register(Instrument)
admin.site.register(Brand)

