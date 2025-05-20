from django.contrib import admin

from .models import Doctor, Service, Appointment, Review, Departments, FAQ, SocialNetwork

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Review)
admin.site.register(Departments)
admin.site.register(FAQ)
admin.site.register(SocialNetwork)
