# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#
from .models import Cancha, Comentarys

#


class CanchaAdmin(admin.ModelAdmin):

    """admin model cancha"""
    list_display = (
        'name',
        'addresse',
        'phone',
        'price_dia',
        'price_noche',
        'techo',
        'parking',
    )
    #
    filter_horizontal = ('zone',)
    search_fields = ('name',)
    list_filter = ('techo','parking','zone',)


class ComentarysAdmin(admin.ModelAdmin):
    """
        model comentarys
    """
    list_display = (
        'cancha',
        'user',
    )
    #

    search_fields = ('cancha', 'user',)
    list_filter = ('cancha','user',)


#admin rgiter
admin.site.register(Cancha, CanchaAdmin)
admin.site.register(Comentarys, ComentarysAdmin)
