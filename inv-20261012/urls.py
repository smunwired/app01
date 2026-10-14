from django.urls import path
from . import views
from django.urls import re_path as url
app_name='inv'
urlpatterns = [
    path('add',views.InstrumentCreateView.as_view(),name='InstrumentCreateView'),
    path('detail/<int:pk>',views.InstrumentDetailView.as_view(),name='InstrumentDetailView'),
    path('edit/<int:pk>',views.InstrumentUpdateView.as_view(),name='InstrumentUpdateView'),
    path('delete/<int:pk>',views.InstrumentDeleteView.as_view(),name='InstrumentDeleteView'),
    path('',views.InstrumentListView.as_view(),name='InstrumentListView'),
    path('manufacturers',views.ManufacturerListView.as_view(),name='ManufacturerListView'),
    path('manufacturers/add',views.ManufacturerCreateView.as_view(),name='ManufacturerCreateView'),
    path('manufacturers/edit/<int:pk>',views.ManufacturerUpdateView.as_view(),name='ManufacturerUpdateView'),
    path('manufacturers/delete/<int:pk>',views.ManufacturerDeleteView.as_view(),name='ManufacturerDeleteView'),
]
