from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ticket
from .forms import customerOnTicket
from .forms import staffOnTicket
from .forms import ticketItem
from .forms import customer

#from .models import Status


def indexView(request):
    """

    """
    context = {}
    return render(request, "Index.html", context)


def successView(request):
    """

    """
    context = {}
    return render(request, "Success.html", context)


def NewTicketView(request):
    """

    """
    # if this is a POST request we need to process the form data.
    if request.method == 'POST':
        #Create a form instance and populate it with data from the request:
        formTicket = ticket(request.POST)
        formCustomerOnTicket = customerOnTicket(request.POST)
        formStaffOnTicket = staffOnTicket(request.POST)
        formTicketItem_item0_ = ticketItem(request.POST, prefix="_item0_")
        formTicketItem_item1_ = ticketItem(request.POST, prefix="_item1_")
        formTicketItem_item2_ = ticketItem(request.POST, prefix="_item2_")
        formTicketItem_item3_ = ticketItem(request.POST, prefix="_item3_")
        formTicketItem_item4_ = ticketItem(request.POST, prefix="_item4_")

        #Check for valid:
        if formTicket.is_valid() and formCustomerOnTicket.is_valid() and formStaffOnTicket.is_valid() \
                and formTicketItem_item0_.is_valid() and formTicketItem_item1_.is_valid() \
                and formTicketItem_item2_.is_valid() and formTicketItem_item3_.is_valid() \
                and formTicketItem_item4_.is_valid():

            #Process the data:
            formTicket = formTicket.save()                                          #Save the ticket.

            formCustomerOnTicket = formCustomerOnTicket.save(commit=False)
            formCustomerOnTicket.ticketID = formTicket                              #Connect the customer to ticket.
            formCustomerOnTicket.save()

            formStaffOnTicket = formStaffOnTicket.save(commit=False)
            formStaffOnTicket.ticketID = formTicket                                 #Connect the staff to ticket.
            formStaffOnTicket.save()


            if formTicketItem_item0_.cleaned_data["itemID"] != None:
                formTicketItem_item0_ = formTicketItem_item0_.save(commit=False)
                formTicketItem_item0_.ticketID = formTicket                             #Connect the items to ticket.
                formTicketItem_item0_.save()

            if formTicketItem_item1_.cleaned_data["itemID"] != None:
                formTicketItem_item1_ = formTicketItem_item1_.save(commit=False)
                formTicketItem_item1_.ticketID = formTicket                             #Connect the items to ticket.
                formTicketItem_item1_.save()

            if formTicketItem_item2_.cleaned_data["itemID"] != None:
                formTicketItem_item2_ = formTicketItem_item2_.save(commit=False)
                formTicketItem_item2_.ticketID = formTicket                             #Connect the items to ticket.
                formTicketItem_item2_.save()

            if formTicketItem_item3_.cleaned_data["itemID"] != None:
                formTicketItem_item3_ = formTicketItem_item3_.save(commit=False)
                formTicketItem_item3_.ticketID = formTicket                             #Connect the items to ticket.
                formTicketItem_item3_.save()

            if formTicketItem_item4_.cleaned_data["itemID"] != None:
                formTicketItem_item4_ = formTicketItem_item4_.save(commit=False)
                formTicketItem_item4_.ticketID = formTicket                             #Connect the items to ticket.
                formTicketItem_item4_.save()

            #Redirect to new URL:
            return HttpResponseRedirect('/ticketing_system/success/')

    #If a GET (or other method), create a blank form.
    else:
        formTicket = ticket()
        formCustomerOnTicket = customerOnTicket()
        formStaffOnTicket = staffOnTicket()
        formTicketItem_item0_ = ticketItem(prefix="_item0_")
        formTicketItem_item1_ = ticketItem(prefix="_item1_")
        formTicketItem_item2_ = ticketItem(prefix="_item2_")
        formTicketItem_item3_ = ticketItem(prefix="_item3_")
        formTicketItem_item4_ = ticketItem(prefix="_item4_")

    return render(request, 'NewTicket.html',
                  {'formTicket': formTicket,
                   "formCustomerOnTicket": formCustomerOnTicket,
                   "formStaffOnTicket": formStaffOnTicket,
                   "formTicketItem_item0_": formTicketItem_item0_,
                   "formTicketItem_item1_": formTicketItem_item1_,
                   "formTicketItem_item2_": formTicketItem_item2_,
                   "formTicketItem_item3_": formTicketItem_item3_,
                   "formTicketItem_item4_": formTicketItem_item4_,
                   })


def NewCustomerView(request):
    """

    """
    # if this is a POST request we need to process the form data.
    if request.method == 'POST':
        #Create a form instance and populate it with data from the request:
        formCustomer = customer(request.POST)

        #Check for valid:
        if formCustomer.is_valid():

            #Process the data:
            formCustomer = formCustomer.save()                                          #Save the ticket.

            #Redirect to new URL:
            return HttpResponseRedirect('/ticketing_system/success/')

    #If a GET (or other method), create a blank form.
    else:
        formCustomer = customer()

    return render(request, 'NewCustomer.html',
                  {'formCustomer': formCustomer,})
