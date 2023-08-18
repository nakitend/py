
# Import the ModelForm class from Django's forms module.
from django.forms import ModelForm

# Import all the models from your application (assuming they are defined in the models.py file).
from .models import *

# Define a ModelForm class for adding/editing Product objects.
class AddForm(ModelForm):
    class Meta:
        # Specify the model that this form is associated with.
        model = SparePart
        
        # Define the fields that will be displayed in the form for the user.
        fields = [
            'received_quantity',
            'branch_name'  # Display a form field for the 'received_quantity' attribute of the Product model.
        ]

# Define a ModelForm class for adding/editing Sale objects.
class SaleForm(ModelForm):
    class Meta:
        # Specify the model that this form is associated with.
        model = Sale
        
        # Define the fields that will be displayed in the form for the user.
        fields = [
            'quantity',  # Display a form field for the 'quantity' attribute of the Sale model.
            'amount_received',  # Display a form field for the 'amount_received' attribute of the Sale model.
            'issued_to',
            'phone_number',
            'date',
            'part_number',
            'part_name' # Display a form field for the 'issued_to' attribute of the Sale model.
        ]

#In this code, you are using Django's `ModelForm` class to create forms for user interaction. These forms are associated with your `Product` and `Sale` models and allow users to input or edit data. The forms are generated based on the fields you specify in the `fields` attribute under the `Meta` class of each form.

#For the `AddForm`, the form provides a field for the `received_quantity` attribute of the `Product` model, allowing users to add or update the received quantity of a product.

#For the `SaleForm`, the form provides fields for the `quantity`, `amount_received`, and `issued_to` attributes of the `Sale` model. These fields allow users to input information related to a sale transaction, including the quantity sold, the amount received, and the entity to which the sale was issued.

#These forms can be used in your views or templates to create user-friendly interfaces for adding and editing data in your Django application.