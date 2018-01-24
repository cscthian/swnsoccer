# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from django.conf import settings
# third-party
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta

#
from .managers import ZoneManager


@python_2_unicode_compatible
class Distrito(TimeStampedModel):
    """ modelo para distrito de un departamento"""

    name = models.CharField('nombre', max_length=130)
    slug = models.SlugField(editable=False, max_length=200)

    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'
        ordering = ['-created']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.name, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.name, str(seconds))

        self.slug = slugify(slug_unique)
        super(Distrito, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Zone(TimeStampedModel):
    """ modelo para zonas de un distrito"""

    distrito = models.ForeignKey(Distrito, verbose_name='Distrito', on_delete=models.CASCADE,)
    name = models.CharField('Nombre', max_length=130)
    slug = models.SlugField(editable=False, max_length=200)

    objects = ZoneManager()

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'
        ordering = ['-created']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.name, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.name, str(seconds))

        self.slug = slugify(slug_unique)
        super(Zone, self).save(*args, **kwargs)
