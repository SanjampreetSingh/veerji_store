# Generated by Django 3.2.9 on 2021-12-08 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20211129_1950'),
        ('product', '0002_auto_20211129_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.category'),
        ),
    ]
