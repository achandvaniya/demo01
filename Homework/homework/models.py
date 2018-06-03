# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class City(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"

class Customer(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField(
                        validators=[
                            MaxValueValidator(10),
                            MinValueValidator(10)
                        ]
                     )
    # Currently, I have only provided support for mobile number, for future enhancement, we can update it so that it can accept, landline and country code etc.
      
    def __str__(self):
        return self.first_name + " " + self.last_name

class Cleaner(BaseModel):
    """docstring for Cleaner"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    quality_score = models.DecimalField(max_digits=10, decimal_places=2)
  
    def __str__(self):
        return self.first_name + " " + self.last_name

class CleanerCityMap(BaseModel):
    Cleaner = models.ForeignKey(Cleaner)
    City = models.ForeignKey(City)

    class Meta:
        unique_together = ('Cleaner', 'City')

    def __str__(self):
        return "{}_{} - {}".format(self.Cleaner.first_name, self.Cleaner.last_name ,self.City.name)
    

class Booking(BaseModel):
    Customer = models.ForeignKey(Customer)
    Cleaner = models.ForeignKey(Cleaner)
    date =  models.DateTimeField()

    def __str__(self):
        return "{} {} -{} {} -{}".format(self.Customer.first_name, self.Customer.last_name ,self.Cleaner.first_name, self.Cleaner.last_name, self.date.strftime("%m-%d-%Y %H:%M"))
    