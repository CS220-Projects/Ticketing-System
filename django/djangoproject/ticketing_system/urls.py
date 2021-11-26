from django.urls import path

from . import views

app_name = "ticketing_system"

urlpatterns = [
    path('new-ticket/', views.newTicketView, name="NewTicket"),
    path('new-customer/', views.newCustomerView, name="NewCustomer"),
    path('details/', views.detailsView, name="Details"),
    path('success/', views.successView, name="SuccessView"),
    path('', views.indexView, name="indexView"),
]
