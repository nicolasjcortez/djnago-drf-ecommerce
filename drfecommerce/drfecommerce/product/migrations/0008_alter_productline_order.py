# Generated by Django 4.2.9 on 2024-02-01 13:19

from django.db import migrations
import drfecommerce.product.fields


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0007_productline_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productline",
            name="order",
            field=drfecommerce.product.fields.OrderField(blank=True),
        ),
    ]
