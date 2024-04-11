from django.db import models
from django.utils import timezone

class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    store_location = models.CharField(max_length=100)
    store_timestamp = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return f"{self.store_id} - {self.store_location} - {self.store_timestamp}"

class Products(models.Model):
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=100)
    product_timestamp = models.DateTimeField(default=timezone.now, null=True)
    
    def __str__(self):
        return f"{self.product_id} - {self.product_name} - {self.store_timestamp}"    


class Sales(models.Model):
    transaction_id = models.IntegerField()
    transaction_date = models.DateField(default=timezone.now, null=True)
    transaction_time = models.TimeField(default=timezone.now, null=True)
    transaction_qty = models.IntegerField(null=True)
    store_id = models.IntegerField(null=True)
    product_id = models.IntegerField(null=True)
    unit_price = models.FloatField()
    product_category = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100, null=True)
    product_detail = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.transaction_id} - {self.transaction_qty} - {self.unit_price} - {self.product_category} - {self.product_name} - {self.product_detail}"
    
