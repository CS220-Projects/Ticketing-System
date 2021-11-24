from django.shortcuts import render
from django.http import HttpResponseRedirect


from .forms import TestForm


#from .models import Status

def index(request):
    context = {}
    return render(request, "index.html", context)





def TestView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    return render(request, 'TestForm.html', {'form': form})