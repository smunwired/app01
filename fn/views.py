from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView, UpdateView, DeleteView

# Create your views here.

from .models import Activity,Venue

class ActivityList(ListView):
    model = Activity
    fields = "__all__"
    paginate_by = 22
    ordering = ['-activity_date']

class ActivityTypeList(ListView):
    model = Activity
    fields = "__all__"
    paginate_by = 22
    ordering = ['-activity_date']
    template_name = 'fn/activity_type_list.html'
    def get_queryset(self):
        type = self.kwargs["pk"]
        queryset = Activity.objects.all().filter(type=type).order_by('-activity_date')
        return queryset

class ActivityListExc(ListView):
#    queryset = Activity.objects.raw("select * from fn_activity where venue_id is null order by activity_date")
    queryset = Activity.objects.filter(venue__isnull=True)
    fields = "__all__"
    ordering = ['-activity_date']

    paginate_by = 22

class ActivityAddView(CreateView):
    fields = "__all__"
    model = Activity
    success_url = "/fn/"

class ActivityUpdateView(UpdateView):
    fields = "__all__"
    model = Activity
    template_name_suffix = "_update_form"
    success_url = "/fn/"

class ActivityDelete(DeleteView):
    model = Activity
    success_url = "/fn/"
    template_name = 'fn/activity_confirm_delete.html'

class VenueList(ListView):
    model = Venue
    fields = "__all__"
    paginate_by = 22
    ordering = ['name']

class VenueAddView(CreateView):
    fields = "__all__"
    model = Venue
    success_url = "/fn/venues"

class VenueUpdateView(UpdateView):
    fields = "__all__"
    model = Venue
    success_url = "/fn/venues"

class VenueDelete(DeleteView):
    model = Venue
    success_url = "/fn/venues"
    template_name = 'fn/venue_confirm_delete.html'

