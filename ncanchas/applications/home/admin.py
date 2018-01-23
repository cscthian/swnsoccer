# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Home, Tag


class HomeAdmin(admin.ModelAdmin):
    #
    list_display = (
        'title',
        'description',
        'banner_title',
        'phone_uno',
        'phone_dos',
        'email',)
    filter_horizontal = (
        'tags',
    )
    search_fields = (
        'titulo',
        'banner_title',
    )
    list_filter = (
        'title',
        'banner_title',
    )


class TagAdmin(admin.ModelAdmin):
    #
    list_display = (
        'name',
   )


admin.site.register(Home, HomeAdmin)
admin.site.register(Tag, TagAdmin)
