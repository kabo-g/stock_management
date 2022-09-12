from django.db import models

# Create your models here.

class Stock(models.Model):
    """
        FIELDS

        category, item_name, quantity, received_quantity, received_by, issue_quantity
        issued_by, issued_to, phone_number, created_by, reorder_level, last_updated, export_to_csv
    """
    category = models.CharField(max_length=255, blank=True, null=True)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    received_quantity = models.IntegerField(null=True, blank=True)
    received_by = models.CharField(max_length=255, blank=True, null=True)
    issue_quantity = models.IntegerField(null=True, blank=True)
    issued_by = models.CharField(max_length=255, blank=True, null=True)
    issued_to = models.CharField(max_length=255, blank=True, null = True)
    phone_number = models.CharField(max_length=255, blank=True, null = True)
    created_by = models.CharField(max_length=255, blank=True, null = True)
    reorder_level = models.IntegerField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now = True)
    export_to_csv = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name + " " + self.category + " " + str(self.quantity)
