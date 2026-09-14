from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView
from bk.models import Agency, Type, Booking, Stage, Flight, Destination
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
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

class TypeDetailView(DetailView):
    model = Type

class TypeFlightDetailView(DetailView):
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

class StageListView(ListView):
    model = Stage

class StageAddView(CreateView):
    fields = "__all__"
    model = Stage
    success_url = reverse_lazy("bk:stage-list")

class StageUpdateView(UpdateView):
    fields = "__all__"
    model = Stage
    success_url = reverse_lazy('bk:stage-list')

class StageDeleteView(DeleteView):
    model = Stage
    success_url = reverse_lazy('bk:stage-list')

class FlightListView(ListView):
    model = Flight

class FlightAddView(CreateView):
    fields = "__all__"
    model = Flight
    success_url = reverse_lazy("bk:flight-list")

class FlightUpdateView(UpdateView):
    fields = "__all__"
    model = Flight
    success_url = reverse_lazy("bk:flight-list")

class FlightDeleteView(DeleteView):
    model = Flight
    success_url = reverse_lazy("bk:flight-list")

class DestinationListView(ListView):
    model = Destination

class DestinationAddView(CreateView):
    fields = "__all__"
    model = Destination
    success_url = reverse_lazy("bk:destination-list")

class DestinationUpdateView(UpdateView):
    fields = "__all__"
    model = Destination
    success_url = reverse_lazy('bk:destination-list')

class DestinationDeleteView(DeleteView):
    model = Destination
    success_url = reverse_lazy("bk:destination-list")

class BookingListView(ListView):
    model = Booking

class BookingDetailView(DetailView):
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

class FlightTypeListView(ListView):
    model = Booking
    template_name = 'bk/flight_booking_list.html'
    def get_queryset(self):
        queryset = Booking.objects.all().filter(type_id=1).order_by('-booking_date')
        return queryset

class CinemaTypeListView(ListView):
    model = Booking
    template_name = 'bk/cinema_booking_list.html'
    def get_queryset(self):
        queryset = Booking.objects.all().filter(type_id=7).order_by('-booking_date')
        return queryset

#class BookingAddView(LoginRequiredMixin,CreateView):
class BookingAddView(CreateView):
    fields = "__all__"
    model = Booking
    success_url = reverse_lazy("bk:booking-list")

class BookingUpdateView(UpdateView):
    fields = "__all__"
    model = Booking
#    success_url = reverse_lazy('bk:cinema-list')
    def get_success_url(self):
        if (self.object.type_id == 1):
            return reverse('bk:flights-booked-list')
        else:
            return reverse('bk:cinema-list')

class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy("bk:booking-list")
