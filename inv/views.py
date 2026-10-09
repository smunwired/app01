from django.shortcuts import render

# Create your views here.
from .models import Instrument, Manufacturer, Country, Image
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView 
import os

    
def GalleryView(request):
    path = '/home/munns/git/app01/inv/static/inv'
    img_list = os.listdir(path)
    return render(request, 'inv/gallery.html', {'images': img_list})

class InstrumentImageAdd(CreateView):
    model = Instrument
    fields = "instrument", "image",
    success_url = "/inv/images"
    def form_valid(self, form):
        title = get_object_or_404(Instrument, pk=self.kwargs.get('instrument_id'))
        form.instance.instrument = instrument
        return super().form_valid(form)

class ImportImageView(CreateView):
        model = Image
        fields = "__all__"
        success_url = "/inv/gallery"

class ImageCreateView(CreateView):
    model = Image
    fields = ['instrument','alt']
    success_url = "/inv/gallery"
    def form_valid(self, form):
        image_name = self.kwargs['name']
        form.instance.name = image_name
        return super().form_valid(form)
	
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
    success_url = "/inv"
	
class InstrumentListView(ListView):
    model = Instrument
    ordering = ['id']
 
class InstrumentDetailView(DetailView):
    model = Instrument

class InstrumentUpdateView(UpdateView):
    model = Instrument
    fields = "__all__"
    success_url = "/inv"

class InstrumentDeleteView(DeleteView):
    model = Instrument
    success_url = "/inv"

#class ImageCreateView(CreateView):
#    model = Image
#    fields = "__all__"
#    success_url = "/inv/images"
	
class ImageListView(ListView):
    model = Image
    ordering = ['id']
 
class ImageDetailView(DetailView):
    model = Image
    model = Instrument

class ImageUpdateView(UpdateView):
    model = Image
    fields = "__all__"
    success_url = "/inv/images"

class ImageDeleteView(DeleteView):
    model = Image
    success_url = "/inv/images"
