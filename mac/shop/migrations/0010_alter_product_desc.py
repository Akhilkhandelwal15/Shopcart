# Generated by Django 4.0.3 on 2022-04-20 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=1000),
        ),
    ]