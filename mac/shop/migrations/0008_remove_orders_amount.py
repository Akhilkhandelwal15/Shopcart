# Generated by Django 4.0.3 on 2022-04-17 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orders_amount_alter_orders_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
    ]