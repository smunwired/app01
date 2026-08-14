from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
#from myapp.forms import RideForm
from django.views.generic.edit import FormView, UpdateView


from .models import Ride, Point, RidePoint
from .forms import DetailsForm, RidePointForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class RideList(LoginRequiredMixin,ListView):
    model = Ride
    fields = "__all__"
    paginate_by = 22
    ordering = ['-dtr']

class RideAddView(LoginRequiredMixin,CreateView):
    fields = "__all__"
    model = Ride
    success_url = "/rides"

class RideUpdateView(LoginRequiredMixin,UpdateView):
    fields = "__all__"
    model = Ride
    template_name_suffix = "_update_form"
    success_url = "/rides"

#def delete(request,pk):
#    Ride.objects.filter(id=pk).delete()
#    return redirect('/rides')
class RideDeleteView(DeleteView):
    model = Ride
    success_url = "/rides"

def ride_edit(request,id):
    if request.method=="POST":
        object=Ride.objects.get(id=id)
        form=DetailsForm(request.POST,instance=object)
        if form.is_valid:
            form.save()
            object=Ride.objects.all() # is this necessary?
            return redirect('/rides')
    else:        
        object=Ride.objects.get(id=id)
        action="ride/edit/"
        return render(request,'rides/ride_detail.html',{'object':object})

def point_list(request):
    points=Point.objects.order_by("short_name")
    return render(request,'rides/point_list.html',{'points':points})
    
def ridepoint_list(request):
    ridepoints=RidePoint.objects.order_by("ride")
    return render(request,'rides/ridepoint_list.html',{'ridepoints':ridepoints})
    
def point_add(request):
    if request.method=="POST":
        snm=request.POST['short_name']
        lnm=request.POST['long_name']
        obj=Point.objects.create(short_name=snm,long_name=lnm)
        obj.save()
        return redirect('/points')
    else:
        model = Ride
        action="add"
        return render(request,'rides/point_detail.html',{'action':action}
                      )
def ridepoint_add(request):
    if request.method=="POST":
        snm=request.POST['short_name']
        lnm=request.POST['long_name']
        obj=Ride.objects.create(short_name=snm,long_name=lnm)
        obj.save()
        return redirect('/points')
    else:
        model = Ride
        action="add"
        return render(request,'rides/point_detail.html',{'action':action})

def point_edit(request,id):
    if request.method=="POST":
        object=Point.objects.get(id=id)
        form=DetailsForm(request.POST,instance=object)
        if form.is_valid:
            form.save()
            object=Point.objects.all() # is this necessary?
            return redirect('/points')
    else:        
        object=Point.objects.get(id=id)
        action="point/edit/"
        return render(request,'rides/point_detail.html',{'object':object})

def ridepoint_edit(request,id):
    if request.method=="POST":
        object=RidePoint.objects.get(id=id)
        form=DetailsForm(request.POST,instance=object)
        if form.is_valid:
            form.save()
            object=RidePoint.objects.all() # is this necessary?
            return redirect('/ridepoints')
    else:        
        object=RidePoint.objects.get(id=id)
        action="ridepoint/edit/"
        return render(request,'rides/ridepoint_detail.html',{'object':object})

def point_delete(request,pk):
    Point.objects.filter(id=pk).delete()
    return redirect('/points')

def ridepoint_delete(request,pk):
    Point.objects.filter(id=pk).delete()
    return redirect('/ridepoints')

def get_ride_point(request):
    if request.method == "POST":
        form = RidePointForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Form submission successful')
            form.save()
            return HttpResponseRedirect("ridepoints")
        else:
            return HttpResponseRedirect("/form-not-valid/")
    else:
        form = RidePointForm()

    return render(request, "rides/ridepoint.html", {"form": form})

from django.views.generic.edit import CreateView

class RidePointCreateView(CreateView):
    model = RidePoint
    fields = "__all__"

    def get_success_url(self):
        return '/ridepoints'
        #return reverse('ridepoints', kwargs={'ridepoint_slug': self.object.ridepoint_slug})
