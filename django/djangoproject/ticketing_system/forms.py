from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput, Select
from django import forms
from django.db import models

from .models import Franchise, Restaurant_Location, Item, Ticket, Customer_On_Ticket, \
    Staff_On_Ticket, Ticket_Item, Staff, Customer


class customerOnTicket(forms.ModelForm):
    """

    """
    class Meta:
        model = Customer_On_Ticket
        fields = ("customerID",)
        widgets = {
            'customerID': Select(attrs={
                'class': "form-select",
                'style': 'margin: 20px;',
            }),
        }


class staffOnTicket(forms.ModelForm):
    """

    """
    class Meta:
        model = Staff_On_Ticket
        fields = ("staffID",)
        widgets = {
            'staffID': Select(attrs={
                'class': "form-select",
                'style': 'margin: 20px;',
            }),
        }


class ticket(ModelForm):
    """

    """
    class Meta:
        model = Ticket
        fields = ("timeToFulfill", "specialRequests", "tip", "completedStatus")
        widgets = {
            'timeToFulfill': NumberInput(attrs={
                'class': "form-control",
                'style': 'margin: 20px',
                'placeholder': '50'
            }),
            'specialRequests': Textarea(attrs={
                'class': "form-control",
                'style': 'margin: 20px',
                'placeholder': 'Extra Sause Please'
            }),
            'tip': NumberInput(attrs={
                'class': "form-control",
                'style': 'margin: 20px;',
                'placeholder': '20'
            }),
            'completedStatus': CheckboxInput(attrs={
                'style': 'width: 20px; height: 20px; margin: 20px;',
            }),
        }
