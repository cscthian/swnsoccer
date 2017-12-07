from django.contrib import admin

# Register your models here.
from .models import Distrito, Zone

admin.site.register(Distrito)
admin.site.register(Zone)
