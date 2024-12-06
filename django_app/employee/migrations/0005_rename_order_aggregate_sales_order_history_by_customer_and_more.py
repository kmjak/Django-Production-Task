# Generated by Django 5.0.2 on 2024-12-06 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='order_aggregate',
            new_name='order_history_by_customer',
        ),
        migrations.AddField(
            model_name='sales',
            name='order_history_by_product',
            field=models.BooleanField(default=True),
        ),
    ]