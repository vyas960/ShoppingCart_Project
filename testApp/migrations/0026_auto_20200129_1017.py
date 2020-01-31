# Generated by Django 3.0.2 on 2020-01-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0025_auto_20200129_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item_detail',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item_image',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='testApp.Product'),
        ),
    ]
