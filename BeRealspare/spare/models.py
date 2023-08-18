
from django.db import models
from django.utils import timezone
# Import necessary modules from Django for defining models and handling time.

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    #day = models.DateField(auto_now_add=True)
    #time = models.TimeField(auto_now_add=True)
    # Define a model called 'Category' with a field 'name' which is a character field.
    # max_length sets the maximum length of the field's content.
    # null=False means the field cannot be empty in the database.
    # blank=False means the field is required in forms.

    def __str__(self):
        return self.name
    # A string representation of the model object, returning the name of the category.

class SparePart(models.Model):
    Category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    # Define a model called 'Product' with a field 'Category_name' which is a foreign key to the 'Category' model.
    # on_delete=models.CASCADE means when a referenced category is deleted, delete this product as well.
    # null=False means the field cannot be empty in the database.
    # blank=False means the field is required in forms.
    date_of_arrvial = models.DateField(default=timezone.now)

    part_name = models.CharField(max_length=50, null=False, blank=False)
    # Define a field 'item_name' for the product, similar to the 'name' in Category.
    
    total_quantity = models.IntegerField(default=0, null=False, blank=False)
    issued_quantity = models.IntegerField(default=0, null=False, blank=False)
    received_quantity = models.IntegerField(default=0, null=False, blank=False)
    # Define fields for keeping track of quantities, with default values of 0.
    
    unit_price = models.IntegerField(default=0, null=False, blank=False)
    # Define a field 'unit_price' for storing the price of the product.
    
    items_orgin = models.CharField(max_length=50, null=False, blank=False)
    branch_name = models.CharField(max_length=100,blank=False)
    # Define a field 'items_orgin' to store the origin of the items.

    def __str__(self):
        return self.part_name
    # A string representation of the model object, returning the item name.

class Sale(models.Model):
    item = models.ForeignKey(SparePart, on_delete=models.CASCADE, null=False, blank=False)
    # Define a model 'Sale' with a field 'item', which is a foreign key to the 'Product' model.
    # on_delete=models.CASCADE means when a referenced product is deleted, delete this sale as well.
    # null=False means the field cannot be empty in the database.
    # blank=False means the field is required in forms.

    quantity = models.IntegerField(default=0, null=False, blank=False)
    amount_received = models.IntegerField(default=0, null=False, blank=False)
    # Define fields for quantity of items sold and amount received for the sale.

    issued_to = models.CharField(max_length=100, null=False, blank=False)
    unit_price = models.IntegerField(default=0, null=False, blank=False)
    phone_number =models.IntegerField(default=0, null=False, blank=False)
    date = models.DateField(default=timezone.now)
    part_number =models.IntegerField(default=0, null=False, blank=False)
    part_name =models.IntegerField(default=0, null=False, blank=False)
    # Define fields for the recipient and the unit price of the sold items.

    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)
    # Define a method to calculate the total amount for the sale.
    
    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))
    # Define a method to calculate the change due for the sale.

    def __str__(self):
        return self.item.item_name
    # A string representation of the model object, returning the item name.