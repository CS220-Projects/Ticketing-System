from django.contrib import admin

from .models import Franchise, RestaurantLocation, Item, Staff

admin.site.register(Franchise)
admin.site.register(RestaurantLocation)
admin.site.register(Item)

admin.site.register(Staff)

