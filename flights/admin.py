from django.contrib import admin

from .models import Airport, Flight, Passenger

# Register your models here.

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)

# Customize admin interface.
class PassengerInline(admin.StackedInline):
    model = Passenger.flights.through
    extra = 1

class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)
