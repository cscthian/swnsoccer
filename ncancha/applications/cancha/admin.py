# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#models
from .models import CampoDeportivo

class CampoDeportivoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'reference',
        'addresse',
        'techo',
        'public',
        'image',
        'pk',
    )
    search_fields = ('name', 'addresse')
    list_filter = ('techo','public',)
    filter_horizontal = ('tag','phone','price',)

admin.site.register(CampoDeportivo,CampoDeportivoAdmin)
