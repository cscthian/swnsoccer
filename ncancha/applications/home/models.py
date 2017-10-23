# -*- coding: utf-8 -*-
# future
from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

# django
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Cancha(TimeStampedModel):
    """modelo reistro de cancha"""

    name = models.CharField('nombre', max_length=300)
    reference = models.TextField('referencia',blank=True)
    distrito = models.CharField('direccion',blank=True, max_length=100)
    techo = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to='portada',
        verbose_name='Subir imagen',
        blank=True,
        null=True,
    )
    maps = models.CharField(blank=True, max_length=500)
    price = models.TextField(blank=True)
    phone = models.TextField(blank=True)
    web = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Inscripcion de Cancha'
        verbose_name_plural = 'Inscripcion de Cancha'

    def __str__(self):
        return self.name



@python_2_unicode_compatible
class Contact(TimeStampedModel):
    """modelo contacto"""

    asunto = models.CharField('asunto', max_length=300)
    mensaje = models.TextField('mensaje',blank=True)
    email = models.EmailField()
    leido = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Bandeja de mensajes'

    def __str__(self):
        return self.asunto
