# Generated by Django 3.0.2 on 2020-01-28 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0019_auto_20200128_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='grandTotal',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
