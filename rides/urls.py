from django.urls import path
from . import views
from django.urls import re_path as url

app_name = "rides"
urlpatterns = [
    path('add',views.RideAddView.as_view(),name='ride_add'),
    path('edit/<pk>',views.RideUpdateView.as_view(),name='ride_edit'),
    path('',views.RideList.as_view(),name="ride_list"),
#    path('delete/<pk>',views.delete,name="delete"),
    path('delete/<pk>',views.RideDeleteView.as_view(),name="delete"),
#    path('add',views.ride_add,name='ride_add'),
#    path('',views.ride_list,name="ride_list"),
#    path('ride/edit/<int:id>',views.ride_edit,name="ride_edit"),
#    url(r'^ride/delete/(?P<pk>[0-9]+)/$', views.delete,name="delete"),
#    path('point/add',views.point_add,name='point_add'),
#    path('ridepoint/add',views.point_add,name='ridepoint_add'),
#    path('points',views.point_list,name="point_list"),    
#    path('ridepoints',views.ridepoint_list,name="ridepoint_list"),    
#    path('point/edit/<int:id>',views.point_edit,name="point_edit"),    
#    path('ridepoint/edit/<int:id>',views.ridepoint_edit,name="ridepoint_edit"),    
#    url(r'^point/delete/(?P<pk>[0-9]+)/$', views.point_delete,name="point_delete"),
#    url(r'^ridepoint/delete/(?P<pk>[0-9]+)/$', views.point_delete,name="ridepoint_delete"),
#    path('get_ride_point',views.get_ride_point,name='get_ride_point'),  
#    path('ridepoint/create',views.RidePointCreateView.as_view(),name='ridepointcreateform'),  
]
