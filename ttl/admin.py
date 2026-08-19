from django.contrib import admin

# Register your models here.
from .models import Artist,Title,Listen,Title_medium,Medium,Image
admin.site.register(Artist)
admin.site.register(Title)
admin.site.register(Listen)
admin.site.register(Medium)
admin.site.register(Title_medium)
admin.site.register(Image)

