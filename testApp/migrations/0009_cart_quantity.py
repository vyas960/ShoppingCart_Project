# Generated by Django 3.0.2 on 2020-01-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0008_auto_20200115_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]