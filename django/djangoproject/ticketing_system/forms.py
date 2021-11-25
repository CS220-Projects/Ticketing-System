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


class ticketItem(forms.ModelForm):
    """

    """
    class Meta:
        model = Ticket_Item
        fields = ("itemID", "quantity", "currentPrice",)
        widgets = {
            'itemID': Select(attrs={
                'style': 'width: 30%; margin: 20px;',
            }),
            'quantity': NumberInput(attrs={
                'class': "form-control",
                'style': 'width: 10%; margin: 20px;',
            }),
            'currentPrice': NumberInput(attrs={
                'class': "form-control",
                'style': 'width: 10%; margin: 20px;',
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

class customer(forms.ModelForm):
    """

    """
    class Meta:
        model = Customer
        fields = ("phoneNumber", "customerName", "gender", )
        widgets = {
            'phoneNumber': NumberInput(attrs={
                'class': "form-control",
                'style': 'margin: 20px',
                'placeholder': '5087937711'
            }),
            'customerName': TextInput(attrs={
                'class': "form-control",
                'style': 'margin: 20px',
                'placeholder': 'Robert H. Goddard'
            }),
            'gender': TextInput(attrs={
                'class': "form-control",
                'style': 'margin: 20px',
                'placeholder': 'Male'
            }),
        }