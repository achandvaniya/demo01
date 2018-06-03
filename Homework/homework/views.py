# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *
from .forms import HomeWorkForm

def index(request):
    context = {}
    context['form'] = HomeWorkForm()
    if request.method == "POST":
        input_form = HomeWorkForm(request.POST)
        if input_form.is_valid():
            first_name = input_form.cleaned_data.get('first_name', None)
            last_name = input_form.cleaned_data.get('last_name', None)
            phone_number = input_form.cleaned_data.get('phone_number', None)
            city = input_form.cleaned_data.get('city', None)
            date = input_form.cleaned_data.get('date', None)
            
            customer = None
            try:
                customer = Customer.objects.get(phone_number=phone_number)
                # If customer first_name and last_name is different, then I am not doing anything at this time.
            except Exception as e:
                # Check for the new customer and sign in them into the system.
                customer = Customer(first_name = first_name, last_name = last_name, phone_number = phone_number)
                customer.save()
            
            cleaners = CleanerCityMap.objects.filter(City__name = city).values_list('Cleaner', flat=True)
            if not cleaners:
                context["info_message"] = "Cleaner is not available at your city"
            else:
                booked_cleaners = Booking.objects.filter(Cleaner__in = cleaners, date = date).values_list('Cleaner', flat=True)            
                available_cleaners = Cleaner.objects.filter(id__in=cleaners).exclude(id__in=booked_cleaners)
                if available_cleaners:
                    booking = Booking(Customer=customer, Cleaner=available_cleaners.first(), date=date)
                    booking.save()
                    context["success_message"] = "Booking is created successfully"
                else:
                    context["info_message"] = "Cleaner is not available at provided date time"
            # We can use Django messages in here
            form = HomeWorkForm()
        else:
            context['form'] = HomeWorkForm()
    return render(request, 'homework/index.html', context)