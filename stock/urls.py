from django.urls import path
from .views import Homepage, AddForm, AddInvoice, ListInvoice
urlpatterns = [
    path("", Homepage.as_view(), name = "home"),
    path("add_item", AddForm.as_view(), name = "add_item"),
    path("add_invoice", AddInvoice.as_view(), name = "add_invoice"),
    path("list", ListInvoice.as_view(), name = "list_invoice"),
]
