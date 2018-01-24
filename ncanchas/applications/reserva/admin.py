from django.contrib import admin

# Register your models here.

from .models import Price, Reservation


class PriceAdmin(admin.ModelAdmin):
    #
    list_display = (
        'cancha',
        'price',
        'description',)
    search_fields = (
        'cancha',
    )
    list_filter = (
        'cancha',
        'price',
    )

class ReservationAdmin(admin.ModelAdmin):
    #
    list_display = (
        'cacha',
        'date',
        'price',
    )
    search_fields = (
        'cacha',
    )

    list_filter = (
        'cacha',
        'price',
    )
admin.site.register(Price, PriceAdmin)
admin.site.register(Reservation, ReservationAdmin)
