from django.contrib import admin
from .models import Stock, Invoice
from .forms import StockForm, InvoiceForm
# Register your models here.

class StockFormAdmin(admin.ModelAdmin):
    list_display = ["item_name", "category", "quantity"]
    form = StockForm
    list_filter =  ["category", "quantity"]
    search_fields = ["category", "item_name"]

class InvoiceFormAdmin(admin.ModelAdmin):
    list_display = ["customer_name", "invoice_date", "invoice_type"]
    form = InvoiceForm
    list_filter =  ["invoice_type", "paid"]
    search_fields = ["customer_name", "quantity"]

admin.site.register(Invoice, InvoiceFormAdmin)

admin.site.register(Stock, StockFormAdmin)
