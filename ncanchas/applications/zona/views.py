# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#django library
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
    TemplateView,
    View,
)

#local
from .models import Distrito, Zone
from .functions import agrupar_distrito_cancha
from .forms import KwordForm


class DistritoListView(ListView):
    """ vista que lita los distritos registrados """

    context_object_name = 'distritos'
    template_name = 'zona/distritos.html'

    def get(self, request, *args, **kwargs):
        #si reconocemos kword saltamos a otra vista
        if len(self.request.GET) > 0:
            url1 = '/cancha-de-gras/?csrfmiddlewaretoken='
            url2 = str(self.request.GET.get('csrfmiddlewaretoken'))+'&kword='+self.request.GET.get('kword')
            return HttpResponseRedirect(url1+url2)
        #
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.") % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(DistritoListView, self).get_context_data(**kwargs)
        #contexto principal
        context['form'] = KwordForm
        return context

    def get_queryset(self):
        #recuperamos pk por url
        return agrupar_distrito_cancha()


class ZoneByDistritoView(ListView):
    """ vista que liste zonas por distrito """

    context_object_name = 'zonas'
    template_name = 'zona/by_distrito.html'

    def get(self, request, *args, **kwargs):
        #si reconocemos kword saltamos a otra vista
        if len(self.request.GET) > 0:
            url1 = '/cancha-de-gras/?csrfmiddlewaretoken='
            url2 = str(self.request.GET.get('csrfmiddlewaretoken'))+'&kword='+self.request.GET.get('kword')
            return HttpResponseRedirect(url1+url2)
        #
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.") % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(ZoneByDistritoView, self).get_context_data(**kwargs)
        #contexto principal
        context['form'] = KwordForm
        context['distrito'] = Distrito.objects.get(
            slug=self.kwargs['slug']
        )
        return context

    def get_queryset(self):
        #recuperamos pk por url
        distrito = self.kwargs['slug']
        queryset = Zone.objects.listar_por_distrito(distrito)
        return queryset


class ZoneLitView(ListView):
    """ vista que liste zonas en orden de numero canchas"""

    context_object_name = 'zonas'
    template_name = 'zona/list.html'

    def get(self, request, *args, **kwargs):
        #si reconocemos kword saltamos a otra vista
        if len(self.request.GET) > 0:
            url1 = '/cancha-de-gras/?csrfmiddlewaretoken='
            url2 = str(self.request.GET.get('csrfmiddlewaretoken'))+'&kword='+self.request.GET.get('kword')
            return HttpResponseRedirect(url1+url2)
        #
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.") % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(ZoneLitView, self).get_context_data(**kwargs)
        #contexto principal
        context['form'] = KwordForm
        return context

    def get_queryset(self):
        #recuperamos pk por url
        queryset = Zone.objects.zonas_mas_populares()
        return queryset
