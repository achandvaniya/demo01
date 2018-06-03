from django import forms
import datetime
from .models import City

class HomeWorkForm(forms.Form):
    first_name = forms.CharField(max_length=20,required=True)
    last_name = forms.CharField(max_length=20,required=True)
    phone_number = forms.IntegerField(required=True)
    city = forms.ModelChoiceField(queryset=City.objects.all().order_by('name'), required=True,label='Select city')
    date= forms.DateTimeField()