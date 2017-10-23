# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#models
from .models import Tag, Price, Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'number',
        'pk',
    )
    search_fields = ('description', 'number')

admin.site.register(Phone,PhoneAdmin)


class PriceAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'value',
        'pk',
    )
    search_fields = ('description', 'value')

admin.site.register(Price,PriceAdmin)
#
admin.site.register(Tag)
