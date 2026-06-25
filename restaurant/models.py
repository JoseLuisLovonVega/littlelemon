from django.db import models


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.DecimalField(max_digits=5, decimal_places=2)
   description = models.TextField(max_length=1000, default='')
   
   def __str__(self): # This method defines the string representation of the Menu model. When a Menu object is printed or displayed in the Django admin interface, it will show the name of the menu item instead of the default representation (which would be something like "Menu object (1)").
      return self.name # This line returns the name of the menu item as the string representation of the Menu model. It allows you to easily identify and display menu items in a human-readable format.
