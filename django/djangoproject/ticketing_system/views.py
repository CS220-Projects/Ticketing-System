from django.shortcuts import render

#from .models import Status

def index(request):
    context = {}
    return render(request, "index.html", context)
