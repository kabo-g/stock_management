from django.urls import path
from .views import Homepage, AddForm
urlpatterns = [
    path("", Homepage.as_view(), name = "home"),
    path("add_item", AddForm.as_view(), name = "add_item"),
]
