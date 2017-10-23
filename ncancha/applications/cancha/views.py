# -*- coding: utf-8 -*-

# django
from django.views.generic import (
    DetailView,
    TemplateView,
    DeleteView,
    UpdateView,
    ListView,
    CreateView,
)
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#local
from .models import CampoDeportivo
from .forms import SearchForm


class IndexListView(ListView):
    """ vista de inicio de pagina """
    context_object_name = 'campos'
    paginate_by = 20
    template_name = 'cancha/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['form'] = SearchForm
        context['option'] = 'todos'
        return context

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        if ((kword =='')or(kword==' ')or(kword=='   ')):
            queryset = CampoDeportivo.objects.filter_camp_techo('todo')
        else:
            queryset = CampoDeportivo.objects.filter_camps(kword,'todo')

        return queryset


class CampoDeportivoListView(ListView):
    """ vista para filtrar campos deportivos """
    context_object_name = 'campos'
    paginate_by = 40
    template_name = 'cancha/search.html'

    def get_context_data(self, **kwargs):
        context = super(CampoDeportivoListView, self).get_context_data(**kwargs)
        context['form'] = SearchForm
        context['option'] = self.kwargs['flat']
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        kword = self.request.GET.get("kword", '')
        flat = self.kwargs['flat']
        #verificamos si hay texto
        if ((kword =='')or(kword==' ')or(kword=='   ')):
            print 'primer caso'
            queryset = CampoDeportivo.objects.filter_camp_techo(flat)
        else:
            print 'segundo caso'
            queryset = CampoDeportivo.objects.filter_camps(kword,flat)

        return queryset


class CampoDeportivoDetailView(DetailView):
    model = CampoDeportivo
    template_name = 'cancha/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CampoDeportivoDetailView, self).get_context_data(**kwargs)
        campo = self.get_object()
        campo.point = campo.point + 1
        campo.save()
        print 'visitas actualizadas'
        return context
