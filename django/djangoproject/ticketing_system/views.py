from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ticket
from .forms import customerOnTicket
from .forms import staffOnTicket

#from .models import Status


def indexView(request):
    """

    """
    context = {}
    return render(request, "index.html", context)


def successView(request):
    """

    """
    context = {}
    return render(request, "success.html", context)


def NewTicketView(request):
    """

    """
    # if this is a POST request we need to process the form data.
    if request.method == 'POST':
        #Create a form instance and populate it with data from the request:
        formTicket = ticket(request.POST)
        formCustomerOnTicket = customerOnTicket(request.POST)
        formStaffOnTicket = staffOnTicket(request.POST)

        #Check for valid:
        if formTicket.is_valid() and formCustomerOnTicket.is_valid() and formStaffOnTicket.is_valid():
            #Process the data:
            formTicket = formTicket.save()                                          #Save the ticket.

            formCustomerOnTicket = formCustomerOnTicket.save(commit=False)
            formCustomerOnTicket.ticketID = formTicket                              #Connect the customer to ticket.
            formCustomerOnTicket.save()

            formStaffOnTicket = formStaffOnTicket.save(commit=False)
            formStaffOnTicket.ticketID = formTicket                                 #Connect the staff to ticket.
            formStaffOnTicket.save()

            #Redirect to new URL:
            return HttpResponseRedirect('/ticketing_system/success/')

    #If a GET (or other method), create a blank form.
    else:
        formTicket = ticket()
        formCustomerOnTicket = customerOnTicket()
        formStaffOnTicket = staffOnTicket()

    return render(request, 'NewTicket.html', {'formTicket': formTicket, "formCustomerOnTicket": formCustomerOnTicket, "formStaffOnTicket": formStaffOnTicket})
