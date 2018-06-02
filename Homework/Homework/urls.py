"""Homework URL Configuration
"""

from django.conf.urls import url, include
from django.contrib import admin
# from allauth.account import views as allauthviews


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('homework.urls',namespace="homework")),
]

