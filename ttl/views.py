from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404


# Create your views here.

from .models import Artist,Title,Listen,Title_medium,Medium,Image

class ArtistList(ListView):
    model = Artist
    ordering = ['indexed_name']

class ArtistListStartswith(ListView):
    model = Artist
    fields = "__all__"
    paginate_by = 22
    ordering = ['indexed_name']

    def get_queryset(self):
        self.startswith = self.kwargs['startswith']
        return Artist.objects.filter(indexed_name__startswith=(self.startswith))

class ArtistDetail(DetailView):
    model = Artist

class ArtistAdd(CreateView):
    model = Artist
    fields = "__all__"
    success_url = "/ttl/artists"
    def get_success_url(self):
        if 'addtitle' in self.request.POST:
        # Access the newly created object's pk directly via self.object.pk
            return reverse('ttl:artist_title_add', kwargs={'artist_id': self.object.pk})
        else:
            return reverse_lazy('ttl:artist_list')



class ArtistUpdate(UpdateView):
    fields = "__all__"
    model = Artist
    success_url = "/ttl/artists"
    template_name="ttl/artist_edit.html"

class ArtistDelete(DeleteView):
    model = Artist
    success_url = "/ttl/artists"
    template_name = 'ttl/artist_confirm_delete.html'


class TitleList(ListView):
    model = Title

class TitleListStartswith(ListView):
    model = Title
    fields = "__all__"
    paginate_by = 22
    ordering = ['indexed_name']

    def get_queryset(self):
        self.startswith = self.kwargs['startswith']
        return Title.objects.filter(indexed_name__startswith=(self.startswith))

class TitleDetail(DetailView):
    model = Title

class TitleAdd(CreateView):
    model = Title
    fields = "__all__"
    success_url = "/ttl/titles"

class TitleImageAdd(CreateView):
    model = Image 
    fields = "url", "alt",
    success_url = "/ttl/titles"
    def form_valid(self, form):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        form.instance.title = title
        return super().form_valid(form)

class TitleListenAdd(CreateView):
    model = Listen
    fields = "listen_date",
    success_url = "/ttl/titles"
    def form_valid(self, form):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        form.instance.title = title
        return super().form_valid(form)

class ArtistTitleAdd(CreateView):
    model = Title
    fields = ['prefix_name','indexed_name','compilation','first_released']
    success_url = "/ttl/titles"
    def get_success_url(self):
        if 'addlisten' in self.request.POST:
        # Access the newly created object's pk directly via self.object.pk
            return reverse('ttl:title_listen_add', kwargs={'title_id': self.object.pk})
        elif 'addimage' in self.request.POST:
        # Access the newly created object's pk directly via self.object.pk
            return reverse('ttl:title_image_add', kwargs={'title_id': self.object.pk})
        else:
            return reverse_lazy('ttl:title_list')
    def form_valid(self, form):
        artist = get_object_or_404(Artist, pk=self.kwargs.get('artist_id'))
        form.instance.artist = artist
        return super().form_valid(form)

class TitleUpdate(UpdateView):
    fields = "__all__"
    model = Title
    success_url = "/ttl/titles"
class TitleDelete(DeleteView):
    model = Title
    template_name = 'ttl/title_confirm_delete.html'
    success_url = "/ttl/titles"

class ListenList(ListView):
    model = Listen

class ListenImageList(ListView):
    fields = "__all__"
    template_name = 'ttl/listen_image_list.html'
    def get_queryset(self):
        return Listen.objects.raw('''select l.id,listen_date,i.title_image,url 
					from ttl_listen l 
					join ttl_title t on t.id=l.title_id 
					join ttl_image i on i.title_id=t.id 
					order by listen_date desc limit 100''')
class ListenDetail(DetailView):
    model = Listen
class ListenAdd(CreateView):
    model = Listen
    fields = "__all__"
    success_url = "/ttl/listens"
class ListenUpdate(UpdateView):
    fields = "__all__"
    model = Listen
    success_url = "/ttl/listens"
class ListenDelete(DeleteView):
    model = Listen
    success_url = "/ttl/listens"
    template_name = 'ttl/listen_confirm_delete.html'

class ImageList(ListView):
    model = Image
    template_name = 'ttl/image_list_new.html'
#    def get_queryset(self):
#       return Image.objects.filter(title_id__isnull=True)

class ImageListOld(ListView):
    model = Image
    template_name = 'ttl/image_list_old.html'

class ImageListStartswith(ListView):
    model = Image
    fields = "__all__"
    paginate_by = 22
    ordering = ['alt']

    def get_queryset(self):
        self.startswith = self.kwargs['startswith']
        return Image.objects.filter(alt_startswith=(self.startswith))

class ImageAdd(CreateView):
    model = Image
    fields = "__all__"
    success_url = "/ttl/images"
class ImageDetail(DetailView):
    model = Image
class ImageUpdate(UpdateView):
    fields = "__all__"
    model = Image
    #template_name_suffix = "_update_form"
    success_url = "/ttl/images"
class ImageDelete(DeleteView):
    model = Image
    success_url = "/ttl"
    template_name = 'ttl/listen_confirm_delete.html'

class TitleMediumList(ListView):
    model = Title_medium
class TitleMediumAdd(CreateView):
    fields = "__all__"
    model = Title_medium
    success_url = "/ttl/listens"
class TitleMediumUpdate(UpdateView):
    fields = "__all__"
    model = Title_medium
    template_name_suffix = "_update_form"
    success_url = "/ttl/title_media"
class TitleMediumDelete(DeleteView):
    model = Title_medium
    template_name = 'ttl/title_medium_confirm_delete.html'
    success_url = "/ttl/title_media"
class ImageAdd(CreateView):
    model = Image
    fields = "__all__"
    success_url = "/ttl/listens"
#class ImageUpdate(UpdateView):
#    fields = "__all__"
#    model = Image
#    #template_name_suffix = "_update_form"
#    success_url = "/ttl/listens"
#class ImageDelete(DeleteView):
#    model = Image
#    success_url = "/ttl/listens"
#    template_name = 'ttl/title_medium_confirm_delete.html'



