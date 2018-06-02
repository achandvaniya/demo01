# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class City(BaseModel):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Customer(BaseModel):
    fist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=18, null=True, blank=True)
    # I have make this field as string so that user can store no like +9112.. , 0921.... etc
      
    def __str__(self):
        return self.fist_name + " " + self.last_name

class Cleaner(BaseModel):
    """docstring for Cleaner"""
    fist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    quality_score = models.DecimalField(max_digits=2, decimal_places=2)
  
    def __str__(self):
        return self.fist_name + " " + self.last_name

class CleanerCityMap(BaseModel):
    Cleaner = models.ForeignKey(Cleaner)
    City = models.ForeignKey(City)
    

class Booking(BaseModel):
    Customer = models.ForeignKey(Customer)
    Cleaner = models.ForeignKey(Cleaner)
    date =  models.DateTimeField()
