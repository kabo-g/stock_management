from django import forms

from .models import Stock, Invoice

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ["item_name", "category", "quantity"]


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ("__all__")
