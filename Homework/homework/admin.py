# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import City, Cleaner, CleanerCityMap
# Register your models here.

admin.site.register(City)
admin.site.register(Cleaner)
admin.site.register(CleanerCityMap)
