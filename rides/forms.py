from django import forms
from .models import Ride, RidePoint

class DetailsForm(forms.ModelForm):
    class Meta:
        model=Ride
        fields="__all__"


class RidePointForm(forms.ModelForm):
    class Meta:
        model = RidePoint
        fields = ['point','dst','tm']
#        fields = '__all__'
