# Generated by Django 3.0.2 on 2020-01-23 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0013_remove_cart_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]