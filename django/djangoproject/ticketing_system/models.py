import uuid

from django.db import models

class Franchise(models.Model):
    franchiseID = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    franchiseName = models.CharField(max_length = 500)
    franchiseLocation = models.CharField(max_length = 500)

    def __str__(self):
        return f"Franchise Name = {self.franchiseName} | Franchise Location = {self.franchiseLocation}"


class RestaurantLocation(models.Model):
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





class Staff(models.Model):
    staffID = models.UUIDField(default = uuid.uuid4, editable = False)
    restaurantID = models.ForeignKey("RestaurantLocation", null=False, on_delete=models.CASCADE,related_name="Restaurant_Manager")
    franchiseID = models.ForeignKey("Franchise", null = False, on_delete = models.CASCADE, related_name = "Restaurant_Manager")
    staffName = models.CharField(max_length = 500)
    staffStartDate = models.DateTimeField(auto_now=True)
    staffTenure = models.CharField(max_length = 500)
    staffGender = models.CharField(max_length = 500)
    staffSalary = models.DecimalField(max_digits = 20, decimal_places = 2)

    def __str__(self):
        return f"Staff Name = {self.staffName}"

