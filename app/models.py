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

# class Sales(models.Model):
#     transaction_id = models.IntegerField(unique=True)
#     transaction_date = models.DateField()
#     transaction_time = models.TimeField()
    