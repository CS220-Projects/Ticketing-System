from django.contrib import admin

from .models import Franchise, Restaurant_Location, Item, Ticket, Staff, \
                    Customer, Ticket_Item, Customer_On_Ticket, Staff_On_Ticket

admin.site.register(Franchise)
admin.site.register(Restaurant_Location)
admin.site.register(Item)
admin.site.register(Ticket)
admin.site.register(Staff)
admin.site.register(Customer)
admin.site.register(Ticket_Item)
admin.site.register(Customer_On_Ticket)
admin.site.register(Staff_On_Ticket)
