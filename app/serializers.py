from rest_framework import serializers
from .models import Store, Products, Sales

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'store_location', 'store_timestamp']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product_id', 'product_name', 'product_timestamp']
        
class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['transaction_id', 'transaction_date', 'transaction_time', 'transaction_qty', 'unit_price', 'product_category', 'product_name', 'product_detail']
        