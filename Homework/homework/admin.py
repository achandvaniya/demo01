# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import City, Cleaner, CleanerCityMap, Booking

# Register your models here.


class CleanerCityMapAdmin(admin.ModelAdmin):
    list_display = ('Cleaner', 'City', )
    list_filter = ('City',)

admin.site.register(City)
admin.site.register(Cleaner)
admin.site.register(CleanerCityMap,CleanerCityMapAdmin)
admin.site.register(Booking)
