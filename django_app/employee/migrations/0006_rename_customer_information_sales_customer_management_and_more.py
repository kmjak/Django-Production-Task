# Generated by Django 5.0.2 on 2024-12-06 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_rename_order_aggregate_sales_order_history_by_customer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='customer_information',
            new_name='customer_management',
        ),
        migrations.RenameField(
            model_name='sales',
            old_name='product_information',
            new_name='order_aggregate_by_customer',
        ),
        migrations.RenameField(
            model_name='sales',
            old_name='stock_information',
            new_name='order_aggregate_management_by_product',
        ),
    ]