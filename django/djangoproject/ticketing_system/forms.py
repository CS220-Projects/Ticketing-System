from django import forms
from django.db import models

from .models import Franchise, Restaurant_Location, Item, Ticket, Customer_On_Ticket, \
    Staff_On_Ticket, Ticket_Item, Staff, Customer


class ticket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ("timeToFulfill", "specialRequests", "completedStatus", "tip")

class customerOnTicket(forms.ModelForm):
    class Meta:
        model = Customer_On_Ticket
        fields = ("customerID",)

class staffOnTicket(forms.ModelForm):
    class Meta:
        model = Staff_On_Ticket
        fields = ("staffID",)
        
        

# class TestForm(forms.Form):
#     subjectTest = forms.CharField(max_length=100)
