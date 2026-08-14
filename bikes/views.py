from django.shortcuts import render

# Create your views here.
from .models import Bike, Manufacturer
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView 

class ManufacturerListView(ListView):
    model = Manufacturer
    ordering = ['badge']
 
class ManufacturerCreateView(CreateView):
        model = Manufacturer
        fields = "__all__"
        success_url = "/bikes/manufacturers"
	
class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url ="/bikes/manufacturers"

class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    success_url ="/bikes/manufacturers"

class BikeCreateView(CreateView):
        model = Bike
        fields = "__all__"
        success_url = "/bikes/"
	
class BikeListView(ListView):
    model = Bike
    ordering = ['id']
 
class BikeDetailView(DetailView):
    model = Bike

 
class BikeUpdateView(UpdateView):
    model = Bike
    fields = "__all__"
    success_url ="/bikes"

class BikeDeleteView(DeleteView):
    model = Bike
    success_url ="/bikes/"
