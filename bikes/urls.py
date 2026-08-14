from django.urls import path
from . import views
from django.urls import re_path as url
app_name='bikes'
urlpatterns = [
    path('/add',views.BikeCreateView.as_view(),name='BikeCreateView'),
    path('/edit/<int:pk>',views.BikeUpdateView.as_view(),name='BikeUpdateView'),
    path('delete/<int:pk>',views.BikeDeleteView.as_view(),name='BikeDeleteView'),
    path('',views.BikeListView.as_view(),name='BikeListView'),
    path('manufacturers',views.ManufacturerListView.as_view(),name='ManufacturerListView'),
    path('manufacturers/add',views.ManufacturerCreateView.as_view(),name='ManufacturerCreateView'),
    path('manufacturers/edit/<int:pk>',views.ManufacturerUpdateView.as_view(),name='ManufacturerUpdateView'),
    path('manufacturers/delete/<int:pk>',views.ManufacturerDeleteView.as_view(),name='ManufacturerDeleteView'),
]
