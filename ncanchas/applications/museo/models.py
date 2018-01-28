# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from django.conf import settings

# standard library
from datetime import timedelta, datetime

# third-party
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

#local apps
from applications.home.models import Tag


@python_2_unicode_compatible
class Museo(TimeStampedModel):
    """ modelo para pagina museo """

    title_seo = models.CharField('titulo SEO', max_length=200, blank=True)
    description_seo = models.TextField('Descripcion SEO', blank=True)
    content = RichTextUploadingField('contenido')
    video = models.TextField(blank=True)
    video_description = models.CharField('descripcion del video', blank=True, max_length=200)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Museo'
        verbose_name_plural = 'Museo'
        ordering = ['-created']

    def __str__(self):
        return self.title_seo


@python_2_unicode_compatible
class Album(TimeStampedModel):
    """ modelo para pagina album """

    title_seo = models.CharField('titulo SEO', max_length=200, blank=True)
    description_seo = models.TextField('Descripcion SEO', blank=True)
    title = models.CharField('titulo', max_length=200)
    image = models.ImageField(upload_to='museo', verbose_name='imagen')
    image2 = models.ImageField(
        upload_to='museo',
        verbose_name='imagen 2',
        blank=True,
        null=True
    )
    image3 = models.ImageField(
        upload_to='museo',
        verbose_name='imagen 3',
        blank=True,
        null=True
    )
    content = RichTextUploadingField('contenido')
    video = models.TextField(blank=True)
    published = models.BooleanField('publicado', default='false')
    author = models.CharField('autor', max_length=200, blank=True)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(editable=False, max_length=250)

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Album'
        ordering = ['-created']

    def __str__(self):
        return self.title

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
            slug_unique = '%s %s' % (self.title, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)
        super(Album, self).save(*args, **kwargs)
