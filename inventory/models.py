from django.db import models

# Parent class to avoid duplicate fields
class BaseProduct(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # This won't create a separate table

    def __str__(self):
        return self.name
    
class StockItem(BaseProduct):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    @property
    def is_available(self):
        return self.quantity > 0  # Encapsulation applied

    def update_stock(self, change):
        """Update stock quantity safely."""
        if self.quantity + change >= 0:
            self.quantity += change
            self.save()
        else:
            raise ValueError("Not enough stock")

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.quantity} in stock"

    def add_stock(self, qty):
        self.quantity += qty
        self.save()

    def reduce_stock(self, qty):
        if qty > self.quantity:
            raise ValueError("Not enough stock available")
        self.quantity -= qty
        self.save()

    @staticmethod
    def search_product(query):
        """Static method to search products."""
        return StockItem.objects.filter(name__icontains=query)

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name