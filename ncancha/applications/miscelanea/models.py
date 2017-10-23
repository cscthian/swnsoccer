# -*- coding: utf-8 -*-
# future
from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

# django
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Phone(TimeStampedModel):
    """modelo telefono"""

    description = models.CharField('descripcion', max_length=50)
    number = models.CharField('numero',max_length=15)

    class Meta:
        verbose_name = 'Telefono'
        verbose_name_plural = 'Telefonos'

    def __str__(self):
        return str(self.description+'-'+self.number)


@python_2_unicode_compatible
class Price(TimeStampedModel):
    """modelo precio"""

    description = models.CharField('descripcion', max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Precio'
        verbose_name_plural = 'Precios'

    def __str__(self):
        return str(self.description+'-'+str(self.value))


@python_2_unicode_compatible
class Tag(TimeStampedModel):
    '''modelo djanog para etiquetas'''

    name = models.CharField('nombre', max_length=150)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
