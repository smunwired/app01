from django.urls import path
from bk.views import TypeListView, TypeAddView, TypeUpdateView, TypeDeleteView, AgencyListView, AgencyAddView, AgencyUpdateView, AgencyDeleteView, BookingListView, BookingAddView, BookingUpdateView, BookingDeleteView

app_name = "bk"
urlpatterns = [
    path("/types", TypeListView.as_view(), name='type-list'),
    path("/type/add", TypeAddView.as_view(), name='type-add'),
    path("/type/delete/<pk>", TypeDeleteView.as_view(), name='type-delete'),
    path("/type/update/<pk>", TypeUpdateView.as_view(), name='type-update'),
    path("/agencies", AgencyListView.as_view(), name='agency-list'),
    path("/agency/add", AgencyAddView.as_view(), name='agency-add'),
    path("/agency/update/<pk>", AgencyUpdateView.as_view(), name='agency-update'),
    path("/agency/delete/<pk>", AgencyDeleteView.as_view(), name='agency-delete'),
    path("/bookings", BookingListView.as_view(), name='booking-list'),
    path("/booking/add", BookingAddView.as_view(), name='booking-add'),
    path("/booking/update/<pk>", BookingUpdateView.as_view(), name='booking-update'),
    path("/booking/delete/<pk>", BookingDeleteView.as_view(), name='booking-delete'),
]
