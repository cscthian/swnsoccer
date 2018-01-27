# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from django.conf import settings
# third-party
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta


@python_2_unicode_compatible
class Tag(TimeStampedModel):
    """ modelo para etiquetas SEO """

    name = models.CharField('nombre', max_length=100)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['-created']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Home(TimeStampedModel):
    """ modelo para la pagina Principal """

    title = models.CharField('titulo', max_length=200, blank=True)
    description = models.TextField('Descripcion', blank=True)
    banner_title = models.CharField('Titulo banner', max_length=200)
    banner_img = models.ImageField('imagen portada', upload_to='home')
    banner_action = models.CharField('boton primario', max_length=200)
    action_url = models.URLField('url para boton primario',blank=True)
    num_new_canchas = models.IntegerField(default=1)
    phone_uno = models.CharField('Telefono 1', max_length=15, blank=True)
    phone_dos = models.CharField('Telefono 2', max_length=15, blank=True)
    email = models.EmailField('Email de contacto')
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'
        ordering = ['-created']

    def __str__(self):
        return self.title
