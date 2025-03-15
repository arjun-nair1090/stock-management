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

    return render(request, 'inventory/add_product.html', {'form': form})

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

