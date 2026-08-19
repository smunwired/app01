from django.db import models
from datetime import datetime    

# Create your models here.

class Artist(models.Model):
    prefix_name=models.CharField(max_length=22, blank=True, null=True)
    indexed_name=models.CharField(max_length=77, blank=True, null=True)
    def __str__(self):
        return self.indexed_name
    @property
    def get_artist(self):
        if self.prefix_name:
            return f"{self.prefix_name} {self.indexed_name}"
        else:
            return self.indexed_name


class Title(models.Model):
    prefix_name=models.CharField(max_length=22, blank=True)
    indexed_name=models.CharField(max_length=77, blank=True, null=True)
    first_released=models.IntegerField(blank=False, null=False, default=0)
    compilation=models.BooleanField(blank=True, null=True)
    artist=models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.indexed_name
    @property
    def get_title(self):
        if self.prefix_name:
            return f"{self.prefix_name} {self.indexed_name}"
        else:
            return self.indexed_name
    class Meta:
        ordering = ['indexed_name']

class Listen(models.Model):
    listen_date=models.DateField(default=datetime.now())
    title=models.ForeignKey(Title, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.listen_date)
    @property
    def get_listen(self):
            return f"{self.title} {self.listen_date}"

class Medium(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Title_medium(models.Model):
    medium=models.ForeignKey(Medium, on_delete=models.CASCADE)
    title=models.ForeignKey(Title, on_delete=models.CASCADE)
    release_year=models.IntegerField(null=True,blank=True)
    label = models.CharField(max_length=55, null=True, blank=True)
    date_added = models.DateField(null=True, blank=True)
    def __str__(self):
    #    return self.title
        return self.label

class Image(models.Model):
    url=models.CharField(max_length=255,null=True,blank=True)
    alt=models.CharField(max_length=255)
    title=models.ForeignKey(Title, on_delete=models.CASCADE)
    title_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.alt

