# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#
from .models import Cancha, Comentarys

#


class CanchaAdmin(admin.ModelAdmin):
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
    search_fields = ('name', 'addresse',)
    list_filter = ('techo','parking','zone',)


#admin rgiter
admin.site.register(Cancha, CanchaAdmin)
admin.site.register(Comentarys)
