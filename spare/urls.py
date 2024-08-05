
# Import necessary functions/classes from Django.
from django.urls import path
from django.contrib.auth import views as auth_views  # Import the authentication views provided by Django.

# Import views from your 'spare' app.
from spare import views 

# Define the URL patterns for your application.
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),  # URL for the index page.
    
    # User's home page
    path('home/', views.home, name='home'),  # URL for the home page.
    
    # View all sales
    path('all_sales/', views.all_sales, name='all_sales'),  # URL to view all sales.
    
    # Product details page
    path('home/<int:product_id>', views.product_details, name='product_detail'),
    # URL for viewing details of a specific product. Uses the product's ID as a parameter.
    
    # Issue items page
    path('issue_items/<str:pk>', views.issue_items, name='issue_items'),
    # URL for issuing items. Uses a primary key as a parameter.
    
    # Add to stock page
    path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'),
    # URL for adding items to stock. Uses a primary key as a parameter.
    
    # Receipt page
    path('receipt/', views.receipt, name='receipt'),  # URL for viewing a receipt.
    
    # Receipt detail page
    path('receipt/<int:receipt_id>', views.receipt_detail, name='receipt_detail'),
    # URL for viewing details of a specific receipt. Uses the receipt's ID as a parameter.
    
    # Login page (using Django's built-in login view)
    path('login/', auth_views.LoginView.as_view(template_name='sparepart/login.html'), name='login'),
    # URL for user login. Renders a login form using the specified template.
    
    # Logout page (using Django's built-in logout view)
    path('logout/', auth_views.LogoutView.as_view(template_name='sparepart/index.html'), name='logout'),
        path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # URL for user logout. Renders the homepage after logging out.
]

#These URL patterns define how different pages and views are accessed within your Django application. The comments provided above explain what each URL is intended for and any additional parameters they might use.