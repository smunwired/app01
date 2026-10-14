from django.shortcuts import render

# Create your views here.
from .models import Instrument, Manufacturer, Country
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
        success_url = "/inv/manufacturers"
	
class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url ="/inv/manufacturers"

class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    success_url ="/inv/manufacturers"

class InstrumentCreateView(CreateView):
        model = Instrument
        fields = "__all__"
        success_url = "/inv/"
	
class InstrumentListView(ListView):
    model = Instrument
    ordering = ['id']
 
class InstrumentDetailView(DetailView):
    model = Instrument

 
class InstrumentUpdateView(UpdateView):
    model = Instrument
    fields = "__all__"
    success_url ="/bikes/"

class InstrumentDeleteView(DeleteView):
    model = Instrument
    success_url ="/bikes/"
