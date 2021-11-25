from django.shortcuts import render
from django.http import HttpResponseRedirect


from .forms import ticket
from .forms import customerOnTicket
from .forms import staffOnTicket


#from .models import Status



def indexView(request):
    context = {}
    return render(request, "index.html", context)

def successView(request):
    context = {}
    return render(request, "success.html", context)






def TestView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        formTicket = ticket(request.POST)
        formCustomerOnTicket = customerOnTicket(request.POST)
        formStaffOnTicket = staffOnTicket(request.POST)

        # check whether it's valid:
        if formTicket.is_valid() and formCustomerOnTicket.is_valid() and formStaffOnTicket.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            formTicket = formTicket.save()

            formCustomerOnTicket = formCustomerOnTicket.save(commit=False)
            formCustomerOnTicket.ticketID = formTicket
            formCustomerOnTicket.save()

            formStaffOnTicket = formStaffOnTicket.save(commit=False)
            formStaffOnTicket.ticketID = formTicket
            formStaffOnTicket.save()

            return HttpResponseRedirect('/ticketing_system/success/')

    # if a GET (or any other method) we'll create a blank form
    else:
        formTicket = ticket()
        formCustomerOnTicket = customerOnTicket()
        formStaffOnTicket = staffOnTicket()

    return render(request, 'TestForm.html', {'formTicket': formTicket, "formCustomerOnTicket": formCustomerOnTicket, "formStaffOnTicket": formStaffOnTicket})
