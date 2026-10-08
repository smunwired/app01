from django.urls import path
from . import views
from django.urls import re_path as url
app_name='inv'
urlpatterns = [
#    path('/image/import',views.ImportImageView,name='import_image'),
    path('',views.InstrumentListView.as_view(),name='instrument_list'),
    path('/instrument/<int:pk>/image/add',views.InstrumentImageAdd.as_view(),name="instrument_image_add"),
    path('/instrument/detail/<int:pk>',views.InstrumentDetailView.as_view(),name="instrument_detail"),
    path('/instrument/add',views.InstrumentCreateView.as_view(),name='instrument_add'),
    path('/instrument/edit/<int:pk>',views.InstrumentUpdateView.as_view(),name='instrument_edit'),
    path('/instrument/delete/<int:pk>',views.InstrumentDeleteView.as_view(),name='instrument_delete'),
    path('/images',views.ImageListView.as_view(),name='image_list'),
    path('/image/<int:pk>/image/add',views.ImageCreateView.as_view(),name="image_add"),
    path('/image/detail/<int:pk>',views.ImageDetailView.as_view(),name="image_detail"),
    path('/image/add',views.ImageCreateView.as_view(),name='image_add'),
    #path(r'^/image/add/(?P<image>\d+)/$',views.ImageCreateView.as_view(),name='import_image'),
    #path('/image/add/<image>',views.ImageCreateView.as_view(),name='import_image'),
    path('/image/add/',views.ImageCreateView.as_view(),name='import_image'),
    path('/image/edit/<int:pk>',views.ImageUpdateView.as_view(),name='image_edit'),
    path('/image/delete/<int:pk>',views.ImageDeleteView.as_view(),name='image_delete'),
    path('/gallery', views.GalleryView, name='gallery_view'),
    path('/gallery/add', views.ImageCreateView.as_view(), name='image_add'),
    path('manufacturers',views.ManufacturerListView.as_view(),name='ManufacturerListView'),
    path('manufacturers/add',views.ManufacturerCreateView.as_view(),name='ManufacturerCreateView'),
    path('manufacturers/edit/<int:pk>',views.ManufacturerUpdateView.as_view(),name='ManufacturerUpdateView'),
    path('manufacturers/delete/<int:pk>',views.ManufacturerDeleteView.as_view(),name='ManufacturerDeleteView'),
]
