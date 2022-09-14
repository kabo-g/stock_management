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


class Invoice(models.Model):

    INVOICE_CHOICES = (
        ("hr", "hr"),
        ("hr", "hr"),
        ("hr", "hr"),
        ("hr", "hr"),
        ("hr", "hr")
    )

    invoice_date = models.DateField(auto_now_add=False, blank = False, null = False)
    invoice_number = models.IntegerField(blank = False, null = False)
    customer_name = models.CharField(max_length=255, blank = False, null = False)
    phone_number = models.CharField(max_length=10, blank = False, null = False)

    line_one = models.CharField(max_length=255, blank = False, null = False)
    line_one_quantity = models.IntegerField(blank = False, null = False)
    line_one_unit_price = models.FloatField(blank = False, null = False)
    line_one_total_price = models.FloatField(blank = False, null = False)

    line_two = models.CharField(max_length=255, blank = False, null = False)
    line_two_quantity = models.IntegerField(blank = False, null = False)
    line_two_unit_price = models.FloatField(blank = False, null = False)
    line_two_total_price = models.FloatField(blank = False, null = False)

    total_price = models.FloatField(blank = False, null = False)
    paid = models.BooleanField(blank = False, null = False, default=None)
    invoice_type = models.CharField(max_length = 100, blank = False, null = False, choices = INVOICE_CHOICES)


    # def __str__(self):
    #     return self.customer_name + ' ' + self.invoice
