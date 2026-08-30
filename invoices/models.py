from django.db import models

class Invoice(models.Model):
    customer_name = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.customer_name}"
