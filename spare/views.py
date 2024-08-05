
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Importing necessary models from your application.
from .models import *

# Importing model forms from your application.
from .forms import *

# Importing filters for query filtering.
from .filters import *

# Importing the login_required decorator from Django to protect views.
from django.contrib.auth.decorators import login_required

# Importing reverse to create URLs.
from django.urls import reverse

# Define your views here.

# View to render the index page and the index page is my landing page.
def index(request):
    return render(request, 'sparepart/index.html')

# View to render the home page and display products with filters.
def home(request):
    products = SparePart.objects.all().order_by('-id')
    product_filters = ProductFilter(request.GET, queryset=products)
    products = product_filters.qs
    return render(request, 'sparepart/home.html', {'products': products, 'product_filters': product_filters})

# View to render the receipt page, displaying sales.
@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request, 'sparepart/receipt.html', {'sales': sales})

# View to render the details of a receipt.
def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id=receipt_id)
    return render(request, 'sparepart/receipt_detail.html', {'receipt': receipt})

# View to add items to stock.
@login_required
def add_to_stock(request, pk):
    issue_items = SparePart.objects.get(id=pk)
    form = AddForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity'])
            issue_items.total_quantity += added_quantity
            issue_items.save()
            return redirect('home')
    return render(request, 'sparepart/add_to_stock.html', {'form': form})

# View to issue items.
@login_required
def issue_items(request, pk):
    issued_items = SparePart.objects.get(id=pk)
    sales_form = SaleForm(request.POST)

    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_items
            new_sale.unit_price = issued_items.unit_price
            new_sale.save()

            issued_quantity = int(request.POST['quantity'])
            issued_items.total_quantity -= issued_quantity
            issued_items.save()

            return redirect('receipt')
    return render(request, 'sparepart/issue_items.html', {'sales_form': sales_form})

# View to show product details.
@login_required
def product_details(request, product_id):
    product = SparePart.objects.get(id=product_id)
    return render(request, 'sparepart/product_detail.html', {'product': product})

# View to display all sales.
def all_sales(request):
    sales = Sale.objects.all()
    total = sum(items.amount_received for items in sales)
    change = sum([items.get_change() for items in sales])
    net = total - change
    return render(request, 'sparepart/all_sales.html', {'sales': sales, 'total': total, 'change': change, 'net': net})