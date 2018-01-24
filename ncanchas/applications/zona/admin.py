from django.contrib import admin

# Register your models here.
from .models import Distrito, Zone

class DistritoAdmin(admin.ModelAdmin):
    #
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )
class ZoneAdmin(admin.ModelAdmin):
    #
    list_display = (
        'name',
        'distrito',
    )
    search_fields = (
        'name',
    )



admin.site.register(Distrito, DistritoAdmin)
admin.site.register(Zone, ZoneAdmin)
