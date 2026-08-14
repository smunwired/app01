from django.urls import path
from . import views
from django.urls import re_path as url

app_name = "fn"
urlpatterns = [
    path('',views.ActivityList.as_view(),name="activity_list"),
    path('type/<pk>',views.ActivityTypeList.as_view(),name="activity_type_list"),
    path('exc',views.ActivityListExc.as_view(),name="activity_list_exc"),
    path('add',views.ActivityAddView.as_view(),name='activity_add'),
    path('edit/<pk>',views.ActivityUpdateView.as_view(),name='activity_edit'),
    path('delete/<pk>',views.ActivityDelete.as_view(),name="activity_delete"),
    path('venues',views.VenueList.as_view(),name="venue_list"),
    path('venue/add',views.VenueAddView.as_view(),name='venue_add'),
    path('venue/edit/<pk>',views.VenueUpdateView.as_view(),name='venue_edit'),
    path('venue/delete/<pk>',views.VenueDelete.as_view(),name="venue_delete"),
]
