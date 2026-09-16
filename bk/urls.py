from django.urls import path
from bk.views import TypeListView, TypeDetailView, TypeFlightDetailView, TypeAddView, TypeUpdateView, TypeDeleteView 
from bk.views import AgencyListView, AgencyAddView, AgencyUpdateView, AgencyDeleteView, DestinationListView, DestinationAddView, DestinationUpdateView, DestinationDeleteView, FlightListView, FlightAddView, FlightUpdateView, FlightDeleteView, StageListView, StageAddView, StageUpdateView, StageDeleteView
from bk.views import BookingListView, BookingDetailView, BookingTypeListView, BookingAddView, BookingUpdateView, BookingDeleteView
from bk.views import FlightTypeListView,CinemaTypeListView
app_name = "bk"
urlpatterns = [
    path("/types", TypeListView.as_view(), name='type-list'),
    path('/type/flights', TypeFlightDetailView.as_view(),name="type-detail-flight"),
    path('/type/<pk>', TypeDetailView.as_view(),name="type-detail"),
    path("/type/add", TypeAddView.as_view(), name='type-add'),
    path("/type/delete/<pk>", TypeDeleteView.as_view(), name='type-delete'),
    path("/type/update/<pk>", TypeUpdateView.as_view(), name='type-update'),
    path("/agencies", AgencyListView.as_view(), name='agency-list'),
    path("/agency/add", AgencyAddView.as_view(), name='agency-add'),
    path("/agency/update/<pk>", AgencyUpdateView.as_view(), name='agency-update'),
    path("/agency/delete/<pk>", AgencyDeleteView.as_view(), name='agency-delete'),
    path("/destinations", DestinationListView.as_view(), name='destination-list'),
    path("/destination/add", DestinationAddView.as_view(), name='destination-add'),
    path("/destination/update/<pk>", DestinationUpdateView.as_view(), name='destination-update'),
    path("/destination/delete/<pk>", DestinationDeleteView.as_view(), name='destination-delete'),
    path("/flights", FlightListView.as_view(), name='flight-list'),
    path("/flight/add", FlightAddView.as_view(), name='flight-add'),
    path("/flight/update/<pk>", FlightUpdateView.as_view(), name='flight-update'),
    path("/flight/delete/<pk>", FlightDeleteView.as_view(), name='flight-delete'),
    path("/stages", StageListView.as_view(), name='stage-list'),
    path("/stage/add", StageAddView.as_view(), name='stage-add'),
    path("/stage/update/<pk>", StageUpdateView.as_view(), name='stage-update'),
    path("/stage/delete/<pk>", StageDeleteView.as_view(), name='stage-delete'),
    path("", BookingListView.as_view(), name='booking-list'),
    path("/bookings", BookingListView.as_view(), name='booking-list'),
    path("/booking/<pk>", BookingDetailView.as_view(), name='booking-detail'),
    path("/bookings/type/<int:pk>", BookingTypeListView.as_view(), name='booking-type-list'),
    path("/booking/add", BookingAddView.as_view(), name='booking-add'),
    path("/booking/detail/<pk>", BookingDetailView.as_view(), name='booking-detail'),
    path("/booking/update/<pk>", BookingUpdateView.as_view(), name='booking-update'),
    path("/booking/delete/<pk>", BookingDeleteView.as_view(), name='booking-delete'),
    path("/cinema", CinemaTypeListView.as_view(), name='cinema-list'),
    path("/flights-booked", FlightTypeListView.as_view(), name='flights-booked-list'),
]
