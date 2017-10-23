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

from .models import Cancha, Contact

from .forms import CanchaForm, ContactForm


class HomeView(TemplateView):
    template_name = 'home/login.html'


class NosotrosTemplateView(TemplateView):
    template_name = 'home/nosotros.html'


class ConfirmView(TemplateView):
    template_name = 'home/mensaje.html'

    def get_context_data(self, **kwargs):
        context = super(ConfirmView, self).get_context_data(**kwargs)
        if self.kwargs.get('flat', 0) == '0':
            context['mensaje'] = 'Su Campo Deportivo Fue Registrado con Exito, En unas horas podra ver su cancha en esta aplicacion'
        else:
            context['mensaje'] = 'Hemos Recibido su mensaje, Gracias por Colaborar con nosotros :)'
        return context


class CanchaCreateView(CreateView):
    form_class = CanchaForm
    success_url = reverse_lazy('home_app:confirmacion',kwargs = {'flat' : '0'})
    template_name = 'home/register_cancha.html'


class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('home_app:confirmacion',kwargs = {'flat' : '1'})
    template_name = 'home/contact.html'
