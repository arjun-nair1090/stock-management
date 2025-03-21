from django.shortcuts import render, get_object_or_404, redirect
from .models import StockItem, Category
from django.contrib import messages
from .forms import UpdateStockForm, StockItemForm, UpdatePriceForm
from .forms import UpdatePriceForm

def stock_list(request):
    """Show all stock items."""
    items = StockItem.objects.all()
    query = request.GET.get('q', '')

    if query:
        items = StockItem.search_product(query)  # Using static method

    return render(request, 'inventory/stock_list.html', {'items': items})


def update_stock(request, item_id):
    """Update stock quantity."""
    item = get_object_or_404(StockItem, id=item_id)
    
    if request.method == "POST":
        form = UpdateStockForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Stock updated successfully!")
            return redirect('stock_list')
        else:
            messages.error(request, "Invalid data entered.")
    
    else:
        form = UpdateStockForm(instance=item)

    return render(request, 'inventory/update_stock.html', {'form': form, 'item': item})

def delete_stock_item(request, item_id):
    item = get_object_or_404(StockItem, id=item_id)
    item.delete()
    return redirect('stock_list')  # Redirect to stock list page after deletion

def add_stock(request):
    if request.method == "POST":
        form = StockItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('stock_list')
        else:
            messages.error(request, "Invalid data entered.")
    
    else:
        form = StockItemForm()

    return render(request, 'inventory/add_stock.html', {'form': form})

def update_price(request, item_id):
    item = get_object_or_404(StockItem, id=item_id)
    if request.method == "POST":
        form = UpdatePriceForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('stock_list')  # Redirect to stock list after update
    else:
        form = UpdatePriceForm(instance=item)
    
    return render(request, 'inventory/update_price.html', {'form': form, 'item': item})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in successfully!')
                return redirect('stock_list')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()

    return render(request, 'inventory/login.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully!')
            return redirect('stock_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'inventory/signup.html', {'form': form})


def home(request):
    return render(request, 'inventory/home.html')
