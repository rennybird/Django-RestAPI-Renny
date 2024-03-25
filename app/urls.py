from django.urls import path
from .views import StoreDetailUpdateDelete, StoreList, ProductDetailUpdateDelete, ProductList, SalesDetailUpdateDelete, SalesList

urlpatterns = [
     path('stores/', StoreList.as_view(), name='store_list'),
     path('stores/<int:store_id>/', StoreDetailUpdateDelete.as_view(), name='store_detail'),
     path('products/', ProductList.as_view(), name='product_list'),
     path('products/<int:product_id>/', ProductDetailUpdateDelete.as_view(), name='product_detail'),
     path('sales/', SalesList.as_view(), name='sales_list'),
     path('sales/<int:transaction_id>/', SalesDetailUpdateDelete.as_view(), name='sales_detail'),
]
