from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView
from bk.models import Agency, Type, Booking
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy

class AgencyListView(ListView):
    model = Agency

#class AgencyAddView(LoginRequiredMixin,CreateView):
class AgencyAddView(CreateView):
    fields = "__all__"
    model = Agency
    success_url = reverse_lazy('bk:agency-list')

class AgencyUpdateView(UpdateView):
    fields = "__all__"
    model = Agency
    success_url = reverse_lazy('bk:agency-list')

class AgencyDeleteView(DeleteView):
    model = Agency
    success_url = reverse_lazy("bk:agency-list")

class TypeListView(ListView):
    model = Type

#class TypeAddView(LoginRequiredMixin,CreateView):
class TypeAddView(CreateView):
    fields = "__all__"
    model = Type
    success_url = reverse_lazy("bk:type-list")

class TypeUpdateView(UpdateView):
    fields = "__all__"
    model = Type
    success_url = reverse_lazy('bk:type-list')

class TypeDeleteView(DeleteView):
    model = Type
    success_url = reverse_lazy("bk:type-list")

class BookingListView(ListView):
    model = Booking

#    def get_queryset(self):
#        self.startswith = self.kwargs['startswith']
#        return Booking.objects.filter(type_startswith=(self.startswith))

class BookingTypeListView(ListView):
    model = Booking
    def get_queryset(self):
        booking_type = self.kwargs["pk"]
        queryset = Booking.objects.all().filter(type_id=booking_type).order_by('-booking_date')
        return queryset

#class BookingAddView(LoginRequiredMixin,CreateView):
class BookingAddView(CreateView):
    fields = "__all__"
    model = Booking
    success_url = reverse_lazy("bk:booking-list")

class BookingUpdateView(UpdateView):
    fields = "__all__"
    model = Booking
    success_url = reverse_lazy('bk:booking-list')

class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy("bk:booking-list")
