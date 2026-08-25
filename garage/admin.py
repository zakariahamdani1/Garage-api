from django.contrib import admin

from .models import Customer, Car, Mechanic, Repair


admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Mechanic)
admin.site.register(Repair)