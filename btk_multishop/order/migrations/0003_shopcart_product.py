# Generated by Django 4.2.7 on 2023-12-01 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_slug'),
        ('order', '0002_order_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product'),
        ),
    ]
