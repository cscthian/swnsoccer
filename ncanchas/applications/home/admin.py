# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Home, Tag

#admn regster
admin.site.register(Home)
admin.site.register(Tag)
