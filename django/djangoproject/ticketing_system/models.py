import uuid

from django.db import models


class Franchise(models.Model):
    franchiseID = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    franchiseName = models.CharField(max_length = 500)
    franchiseLocation = models.CharField(max_length = 500)

    def __str__(self):
        return f"Franchise Name = {self.franchiseName} | Franchise Location = {self.franchiseLocation}"


class Restaurant_Location(models.Model):
    class Meta:
        unique_together = (('franchiseID','restaurantID'),)

    franchiseID = models.ForeignKey("Franchise", null = False, on_delete = models.CASCADE, related_name = "Restaurant_Franchise")
    restaurantID = models.UUIDField(default = uuid.uuid4, editable = False)
    ManagerID = models.ForeignKey("Staff", blank = True, null = True, on_delete = models.CASCADE, related_name = "Restaurant_Manager")
    restaurantLocation = models.CharField(max_length = 500)
    restaurantName = models.CharField(max_length = 500)

    def __str__(self):
        return f"Restaurant Name = {self.restaurantName} | Restaurant Location = {self.restaurantLocation}"


class Item(models.Model):
    itemID = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    itemName = models.CharField(max_length = 500)
    itemPrice = models.DecimalField(max_digits = 20, decimal_places = 2)

    def __str__(self):
        return f"Item = {self.itemName} | Price = {self.itemPrice}"


class Ticket(models.Model):
    ticketID = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    timeToFulfill = models.DecimalField(max_digits = 20, decimal_places = 2, verbose_name = "Time To Fulfill (Minutes)")
    specialRequests = models.CharField(max_length = 500, verbose_name = "Special Requests")
    completedStatus = models.BooleanField(default = False, verbose_name = "Order Completed")
    orderDate = models.DateTimeField(auto_now = True, verbose_name = "Order Date")
    tip = models.DecimalField(max_digits = 20, decimal_places = 2, verbose_name = "Tip (Percentage)")

    def __str__(self):
        return f"Ticket ID = {self.ticketID} | Order Date = {self.orderDate}"


class Customer_On_Ticket(models.Model):
    class Meta:
        unique_together = (('ticketID','customerID'),)

    ticketID = models.ForeignKey("Ticket", null = False, on_delete = models.CASCADE, related_name = "Customer_On_Ticket")
    customerID = models.ForeignKey("Customer", null = False, on_delete = models.CASCADE, related_name = "Customer_On_Ticket", verbose_name = "Customer Ticket Belongs To")

    def __str__(self):
        return f"Ticket ID = {self.ticketID} | Customer ID = {self.customerID}"


class Staff_On_Ticket(models.Model):
    class Meta:
        unique_together = (('ticketID','staffID'),)

    ticketID = models.ForeignKey("Ticket", null = False, on_delete = models.CASCADE, related_name = "Staff_On_Ticket")
    staffID = models.ForeignKey("Staff", null = False, on_delete = models.CASCADE, related_name = "Staff_On_Ticket", verbose_name = "Staff Member Servicing Ticket")

    def __str__(self):
        return f"Ticket ID = {self.ticketID} | Customer ID = {self.staffID}"


class Ticket_Item(models.Model):
    class Meta:
        unique_together = (('ticketID','itemID'),)

    ticketID = models.ForeignKey("Ticket", null = False, on_delete = models.CASCADE, related_name = "Item_Ticket")
    itemID = models.ForeignKey("Item", null = False, on_delete = models.CASCADE, related_name = "Item_Ticket", verbose_name = "Item", blank = True)
    currentPrice = models.DecimalField(max_digits = 20, decimal_places = 2, verbose_name = "Current Price", blank = True)
    quantity = models.IntegerField(verbose_name = "Quantity", blank = True)

    def __str__(self):
        return f"ticketID = {self.ticketID} | itemID = {self.itemID}"



class Staff(models.Model):
    class Meta:
        unique_together = (('staffID','restaurantID','franchiseID'),)

    staffID = models.UUIDField(default = uuid.uuid4, editable = False)
    restaurantID = models.ForeignKey("Restaurant_Location", null = False, on_delete = models.CASCADE, related_name = "Restaurant_Staff")
    franchiseID = models.ForeignKey("Franchise", null = False, on_delete = models.CASCADE, related_name = "Restaurant_Staff")
    staffName = models.CharField(max_length = 500)
    staffStartDate = models.DateTimeField(auto_now = True)
    staffTenure = models.CharField(max_length = 500)
    staffGender = models.CharField(max_length = 500)
    staffSalary = models.DecimalField(max_digits = 20, decimal_places = 2)

    def __str__(self):
        return f"{self.staffName}"


class Customer(models.Model):
    customerID = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    phoneNumber = models.BigIntegerField(verbose_name = "Customer Phone Number")
    customerName = models.CharField(max_length = 100, verbose_name = "Customer Name")
    gender = models.CharField(max_length = 20, verbose_name = "Customer Gender")

    def __str__(self):
        return f"{self.customerName}"
