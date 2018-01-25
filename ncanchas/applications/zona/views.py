# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#django library
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
    TemplateView,
    View,
)

from .models import Distrito, Zone
from .functions import agrupar_distrito_cancha


class DistritoListView(ListView):
    """ vista que lita los distritos rgistrados """

    context_object_name = 'distritos'
    template_name = 'zona/distritos.html'

    def get_queryset(self):
        #recuperamos pk por url
        return agrupar_distrito_cancha()


class ZoneByDistritoView(ListView):
    """ vista que liste zonas por distrito """

    context_object_name = 'zonas'
    template_name = 'zona/by_distrito.html'

    def get_queryset(self):
        #recuperamos pk por url
        distrito = self.kwargs['slug']
        queryset = Zone.objects.listar_por_distrito(distrito)
        return queryset
