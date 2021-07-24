from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import College, Building, Contacts, Room
# Register your models here.

admin.site.register(College)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Contacts)
