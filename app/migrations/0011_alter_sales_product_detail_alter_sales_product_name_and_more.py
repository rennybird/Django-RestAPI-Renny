# Generated by Django 4.2 on 2024-04-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_sales_product_id_sales_store_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='product_detail',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='product_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='transaction_qty',
            field=models.IntegerField(null=True),
        ),
    ]
