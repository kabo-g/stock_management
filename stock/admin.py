from django.contrib import admin
from .models import Stock
from .forms import StockForm
# Register your models here.

class StockFormAdmin(admin.ModelAdmin):
    list_display = ["item_name", "category", "quantity"]
    form = StockForm
    list_filter =  ["category", "quantity"]
    search_fields = ["category", "item_name"]

admin.site.register(Stock, StockFormAdmin)
