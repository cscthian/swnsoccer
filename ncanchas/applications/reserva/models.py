# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from django.conf import settings
# third-party
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta
#  app cancha
from applications.cancha.models import Cancha


@python_2_unicode_compatible
class Price(TimeStampedModel):
    """ Precio por hora de una cancha """

    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE,)
    price = models.DecimalField('Monto', max_digits=5, decimal_places=2)
    description = models.CharField('Descripcion', max_length=100)

    class Meta:
        verbose_name = 'Precio'
        verbose_name_plural = 'Precios'
        ordering = ['-created']

    def __str__(self):
        return self.cancha.name


@python_2_unicode_compatible
class Reservation(TimeStampedModel):
    """ Recervacion de una cancha """

    cacha = models.ForeignKey(Cancha, on_delete=models.CASCADE,)
    date = models.DateField('Fecha de Reserva')
    hour_start = models.TimeField()
    hour_end = models.TimeField()
    price = models.DecimalField('Precio por hora', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Reservacion'
        verbose_name_plural = 'Reservaciones'
        ordering = ['-created']

    def __str__(self):
        return self.cancha.name
