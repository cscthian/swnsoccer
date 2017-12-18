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

#local app
from .models import Cancha

class CanchaDetailView(DetailView):
    model = Cancha
    template_name = "cancha/detail.html"