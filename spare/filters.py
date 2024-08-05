
# Import the django_filters module, which provides tools for creating dynamic filters for Django models.
import django_filters

# Import all the models from your application (assuming they are defined in the models.py file).
from .models import *

# Define a custom filter class for the Product model.
class ProductFilter(django_filters.FilterSet):
    class Meta:
        # Specify the model that this filter class is associated with.
        model = SparePart
        
        # Define the fields that you want to create filters for in the Product model.
        fields = [
            'part_name'  # Create a filter for the 'item_name' field of the Product model.
        ]

# Define another custom filter class for the Category model.
class CategoryFilter(django_filters.FilterSet):
    class Meta:
        # Specify the model that this filter class is associated with.
        model = Category
        
        # Define the fields that you want to create filters for in the Category model.
        fields = [
            'name'  # Create a filter for the 'name' field of the Category model.
        ]

#In this code, you are using the `django_filters` module to create custom filter classes for your Django models `Product` and `Category`. These filter classes allow you to easily apply filters to querysets of your models, helping you retrieve specific subsets of data based on filter criteria. The filters will be accessible through the query parameters of your API or views.

#The `ProductFilter` class creates a filter for the `item_name` field of the `Product` model, while the `CategoryFilter` class creates a filter for the `name` field of the `Category` model. These filters can be used to perform searches and filtering operations in your Django application.