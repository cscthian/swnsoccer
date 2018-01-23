# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from django.conf import settings
# third-party
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta

#from application Zone
from applications.zona.models import Zone

#managers for cancha
from .managers import CanchaManager

@python_2_unicode_compatible
class Cancha(TimeStampedModel):
    """ modelo para campos deportivos"""

    name = models.CharField('nombre', max_length=130)
    image = models.ImageField('imagen cancha', upload_to='canchas')
    addresse = models.CharField('direccion', max_length=130)
    phone = models.CharField('telefonos', max_length=50, blank=True)
    price_dia = models.DecimalField('Precio de Dia', max_digits=5, decimal_places=2)
    price_noche = models.DecimalField('Precio de Noche', max_digits=5, decimal_places=2)
    description = models.TextField('Descripcion', blank=True)
    mapa = models.TextField('url de google maps', blank=True)
    latitude = models.CharField('Latitud', blank=True, max_length=30)
    longitude = models.CharField('Longitud', blank=True, max_length=30)
    number_player = models.IntegerField('Jugadores or equipo', default=5)
    techo = models.BooleanField('Con techo', default=False)
    sudaderas = models.BooleanField('Presta sudaderas', default=False)
    parking = models.BooleanField('Tiene parque de estacionamiento', default=False)
    cafetin = models.BooleanField('Cuenta con cafetin', default=False)
    sshh = models.BooleanField('Cuenta con SS.HH.', default=False)
    web_url = models.URLField('URL pagina web o Fane Page', blank=True)
    points = models.DecimalField(max_digits=10, decimal_places=3, default=0, editable=False)
    vists = models.IntegerField(default=0, editable=False)
    state = models.BooleanField('Activado', default=False)
    anulate = models.BooleanField('Eliminado', default=False)
    zone = models.ManyToManyField(Zone)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="usuario_cancha",
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(editable=False, max_length=200)

    objects = CanchaManager()

    class Meta:
        verbose_name = 'Campo Deportivo'
        verbose_name_plural = 'Campos Deportivos'
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
        super(Cancha, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Comentarys(TimeStampedModel):
    """ modelo para comentarios de una cancha"""

    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE,)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="usuario_cancha_comentario",
        on_delete=models.CASCADE,
    )
    comentary = models.TextField('Comentario')

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-created']

    def __str__(self):
        return self.comentary
