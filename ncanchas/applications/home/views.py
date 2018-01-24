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

# import app canchas
from applications.cancha.models import Cancha

# import local app
from .models import Home
from .forms import KwordForm
#

class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
    	context = super(HomeView, self).get_context_data(**kwargs)
    	#recuperamos pagina principal de la bd
    	context['home'] = Home.objects.all()[0]
    	context['form'] = KwordForm
    	context['canchas'] = Cancha.objects.filter(
    	   state = True
    	)
    	return context


class PlantillaView(TemplateView):
    template_name = 'plantilla/categories.html'
