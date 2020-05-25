from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from photo.models import Photo


class GalleryList(LoginRequiredMixin, View):
    def get(self, request):
        photos = Photo.objects.all()
        
        page = request.GET.get('page', 1)
        paginator = Paginator(photos, 10)
        try:
            photos = paginator.page(page)
        except PageNotAnInteger:
            photos = paginator.page(1)
        except EmptyPage:
            photos = paginator.page(paginator.num_pages)
    
        return render(request, 'gallery/photo_list.html', { 'photos': photos })

    