from django.contrib import admin

# Register your models here.

from .models import Price, Reservation

admin.site.register(Price)
admin.site.register(Reservation)
