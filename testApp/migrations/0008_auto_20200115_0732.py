# Generated by Django 3.0.2 on 2020-01-15 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0007_auto_20200115_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='grand_total',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]
