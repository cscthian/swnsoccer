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
from django.views.generic.edit import FormView

#local app
from .models import Cancha
from .forms import SearchForm, ComentarysForm


class SearchCanchaView(ListView):
    """ vista que busca canchas"""

    context_object_name = 'canchas'
    template_name = 'cancha/index.html'

    def get_context_data(self, **kwargs):
        context = super(SearchCanchaView, self).get_context_data(**kwargs)
        context['form'] = SearchForm
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        q = self.request.GET.get("kword", '')
        queryset = Cancha.objects.search_cancha(q)
        return queryset


class CanchaDetailView(FormView):
    template_name = "cancha/detail.html"
    form_class = ComentarysForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(CanchaDetailView, self).get_context_data(**kwargs)
        #recuperamos la cancha
        cancha = Cancha.objects.get(slug=self.kwargs['slug'])
        context['cancha'] = cancha
        context['canchas'] = Cancha.objects.relations_canchas(cancha)
        return context

    def form_valid(self, form):
        print('codigo pendiente')
        return super(CanchaDetailView, self).form_valid(form)
