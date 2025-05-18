from django.contrib import admin

from clinic.models import Doctor, Service, Appointment, Review

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Review)
