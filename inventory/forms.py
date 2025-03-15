from django import forms
from .models import StockItem

class StockItemForm(forms.ModelForm):
    class Meta:
        model = StockItem
        fields = ['name', 'category', 'price', 'quantity']

class UpdateStockForm(forms.ModelForm):
    class Meta:
        model = StockItem
        fields = ['quantity']

    def clean_quantity(self):
        """Ensure stock quantity is not negative."""
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise forms.ValidationError("Stock cannot be negative!")
        return quantity

class UpdatePriceForm(forms.ModelForm):
    class Meta:
        model = StockItem
        fields = ['price']