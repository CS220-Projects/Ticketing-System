from django.urls import path

from . import views

app_name = "ticketing_system"

urlpatterns = [
    path('new-ticket/', views.NewTicketView, name="NewTicket"),
    path('new-customer/', views.NewCustomerView, name="NewCustomer"),
    path('success/', views.successView, name="SuccessView"),
    path('', views.indexView, name="indexView"),
]
