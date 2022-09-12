from django import forms

from .models import Stock

class StockForm(forms.ModelForm):

    model = Stock
    fields = ["item_name", "category", "quantity"]
