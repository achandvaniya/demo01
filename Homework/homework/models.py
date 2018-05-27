# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # One on One field to store additional data over all auth user, we also can override django all auth user.
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)

    class Meta:
        verbose_name = 'User profile'

    def __str__(self):
        return "%s - %s "%(self.user.username)

class City(models.Model):
  name = models.CharField(max_length=255)
  
  def __str__(self):
    return self.name
