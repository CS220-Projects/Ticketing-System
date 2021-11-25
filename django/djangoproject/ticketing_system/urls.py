from django.urls import path

from . import views

urlpatterns = [
    path('new-ticket/', views.NewTicketView, name="NewTicket"),
    path('success/', views.successView, name="SuccessView"),
    path('', views.indexView, name="indexView"),
]
