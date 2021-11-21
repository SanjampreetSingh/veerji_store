# Generated by Django 3.2.9 on 2021-11-21 15:22

from django.db import migrations
import django.utils.timezone
import utils.model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='created',
            field=utils.model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='customers',
            name='modified',
            field=utils.model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]
