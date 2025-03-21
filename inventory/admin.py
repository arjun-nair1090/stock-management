from django.contrib import admin
from .models import StockItem

@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "quantity", "created_at")
    search_fields = ("name", "category")
    list_filter = ("category",)

