# Generated by Django 5.1.5 on 2025-01-25 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_product_category_remove_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]
