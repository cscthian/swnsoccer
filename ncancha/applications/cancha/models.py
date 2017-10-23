# -*- coding: utf-8 -*-
# future
from __future__ import unicode_literals

# standard library
from datetime import timedelta, datetime

# third-party
from model_utils.models import TimeStampedModel

# django
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify

#application miscelanea
from applications.miscelanea.models import Tag, Phone, Price

#managers
from .managers import CampoManager


@python_2_unicode_compatible
class CampoDeportivo(TimeStampedModel):
    """modelo campor deportivo"""

    name = models.CharField('nombre', max_length=300)
    reference = models.TextField('referencia',blank=True)
    addresse = models.CharField('direccion',blank=True, max_length=100)
    techo = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to='portada',
        verbose_name='Subir imagen',
        blank=True,
        null=True,
    )
    maps = models.CharField(blank=True, max_length=500)
    tag = models.ManyToManyField(
        Tag,
        verbose_name='tag',
        blank=True,
    )
    price = models.ManyToManyField(
        Price,
        verbose_name='precios',
        blank=True,
    )
    phone = models.ManyToManyField(
        Phone,
        verbose_name='telefonos',
        blank=True,
    )
    point = models.IntegerField(default=0)
    public = models.BooleanField(default=True)
    slug = models.SlugField(editable=False)

    objects = CampoManager()

    class Meta:
        verbose_name = 'Campo Deportivo'
        verbose_name_plural = 'Campos Deportivos'

    def __str__(self):
        return self.name

    #funcion que se ejecuta al guardar
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
        #
        super(CampoDeportivo, self).save(*args, **kwargs)
