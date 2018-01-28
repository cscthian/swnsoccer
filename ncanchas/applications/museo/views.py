# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#django library
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    DetailView,
    ListView,
    TemplateView,
    View,
)

# import local app
from .models import Museo, Album
#

class MuseoView(TemplateView):
    template_name = 'museo/index.html'

    def get_context_data(self, **kwargs):
        context = super(MuseoView, self).get_context_data(**kwargs)
        #contexto principal
        context['museo'] = Museo.objects.all()[0]
        context['albums'] = Album.objects.filter(
            published=True,
        ).order_by('-created')
        return context


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'museo/album.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        context['albums'] = Album.objects.filter(
            published=True,
        ).order_by('-created')[:4]
        return context
