# Generated by Django 3.2.9 on 2021-11-29 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_rename_desciption_category_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='vj_category',
        ),
    ]
