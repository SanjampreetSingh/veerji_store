# Generated by Django 3.2.9 on 2021-12-10 14:27

from django.db import migrations, models
import django.utils.timezone
import utils.model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', utils.model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', utils.model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Localities',
                'db_table': 'vj_locality',
            },
        ),
    ]
