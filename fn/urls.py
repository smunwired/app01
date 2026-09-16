from django.urls import path
from . import views
from django.urls import re_path as url

app_name = "fn"
urlpatterns = [
    path('',views.ActivityListView.as_view(),name="activity-list"),
    path('/add',views.ActivityCreateView.as_view(),name='activity-create'),
    path('/edit/<pk>',views.ActivityUpdateView.as_view(),name='activity-update'),
    path('/delete/<pk>',views.ActivityDeleteView.as_view(),name='activity-delete'),
    path('/exc',views.ActivityListExc.as_view(),name="activity-list-exc"),
    path('/type/<pk>',views.ActivityTypeList.as_view(),name="activity-type-list"),
    path('venues',views.VenueListView.as_view(),name="venue-list"),
    path('venue/add',views.VenueCreateView.as_view(),name='venue-add'),
    path('venue/edit/<pk>',views.VenueUpdateView.as_view(),name='venue-edit'),
    path('venue/delete/<pk>',views.VenueDeleteView.as_view(),name="venue-delete"),
]
