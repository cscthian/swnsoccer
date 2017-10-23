# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Cancha, Contact


class CanchaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'reference',
        'distrito',
        'techo',
        'pk',
    )
    search_fields = ('name','distrito')
    list_filter = ('techo',)

admin.site.register(Cancha,CanchaAdmin)
admin.site.register(Contact)
