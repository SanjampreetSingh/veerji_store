# Generated by Django 3.2.9 on 2021-12-21 18:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recurring_product', '0002_recurringproduct_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurringproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='recurringproduct',
            name='product',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.JSONField(), size=None),
        ),
    ]
