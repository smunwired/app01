from django import forms
from .models import Bike, Manufacturer

class BikeDetailsForm(forms.ModelForm):
    class Meta:
        model=Bike
        fields="__all__"

class ManufacturerDetailsForm(forms.ModelForm):
    class Meta:
        model=Manufacturer
        fields="__all__"