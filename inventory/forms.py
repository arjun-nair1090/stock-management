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

#Login
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

#Sign up
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(max_length=100, label="First Name", required=True)
    last_name = forms.CharField(max_length=100, label="Last Name", required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
