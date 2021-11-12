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
    ManagerID = models.ForeignKey("Staff", null = True, on_delete = models.CASCADE, related_name = "Restaurant_Manager")
    restaurantLocation = models.CharField(max_length = 500)
    restaurantName = models.CharField(max_length = 500)

    def __str__(self):
        return f"Restaurant Name = {self.restaurantName} | Restaurant Location = {self.restaurantLocation}"


class Item(models.Model):
    itemID = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    itemName = models.CharField(max_length = 500)
    itemPrice = models.DecimalField(max_digits = 20, decimal_places = 2)

    def __str__(self):
        return f"Item Name = {self.itemName} | Item Price = {self.itemPrice}"


class Ticket(models.Model):
    ticketID = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    timeToFulfill = models.DecimalField(max_digits = 20, decimal_places = 2)
    specialRequests = models.CharField(max_length = 500)
    completedStatus = models.BooleanField(default = False)
    orderDate = models.DateTimeField(auto_now_add = True)
    tip = models.DecimalField(max_digits = 20, decimal_places = 2)

    def __str__(self):
        return f"Ticket ID = {self.ticketID} | orderDate = {self.orderDate}"


class Staff(models.Model):
    class Meta:
        unique_together = (('staffID','restaurantID','franchiseID'),)

    staffID = models.UUIDField(default = uuid.uuid4, editable = False)
    restaurantID = models.ForeignKey("Restaurant_Location", null=False, on_delete=models.CASCADE,related_name="Restaurant_Manager")
    franchiseID = models.ForeignKey("Franchise", null = False, on_delete = models.CASCADE, related_name = "Restaurant_Manager")
    staffName = models.CharField(max_length = 500)
    staffStartDate = models.DateTimeField(auto_now=True)
    staffTenure = models.CharField(max_length = 500)
    staffGender = models.CharField(max_length = 500)
    staffSalary = models.DecimalField(max_digits = 20, decimal_places = 2)

    def __str__(self):
        return f"Staff Name = {self.staffName}"


class Customer(models.Model):
    customerID = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    phoneNumber = models.IntegerField()
    customerName = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 20)

    def __str__(self):
        return f"Customer Name = {self.customerName}"


class Ticket_Item(models.Model):
    class Meta:
        unique_together = (('ticketID','itemID'),)

    ticketID = models.ForeignKey("Ticket",null=False,on_delete=models.CASCADE,related_name="Item_Ticket")
    itemID = models.ForeignKey("Item",null=False,on_delete=models.CASCADE,related_name="Item_Ticket")
    currentPrice = models.DecimalField(max_digits = 20, decimal_places = 2)
    quantity = models.IntegerField()

    def __str__(self):
        return f"ticketID = {self.ticketID} | itemID = {self.itemID}"


class Customer_On_Ticket(models.Model):
    class Meta:
        unique_together = (('ticketID','customerID'),)

    ticketID = models.ForeignKey("Ticket",null=False,on_delete=models.CASCADE,related_name="Customer_On_Ticket")
    customerID = models.ForeignKey("Customer",null=False,on_delete=models.CASCADE,related_name="Customer_On_Ticket")

    def __str__(self):
        return f"Ticket ID = {self.ticketID} | Customer ID = {self.customerID}"


class Staff_On_Ticket(models.Model):
    class Meta:
        unique_together = (('ticketID','staffID'),)

    ticketID = models.ForeignKey("Ticket",null=False,on_delete=models.CASCADE,related_name="Staff_On_Ticket")
    staffID = models.ForeignKey("Staff",null=False,on_delete=models.CASCADE,related_name="Staff_On_Ticket")

    def __str__(self):
        return f"Ticket ID = {self.ticketID} | Customer ID = {self.staffID}"