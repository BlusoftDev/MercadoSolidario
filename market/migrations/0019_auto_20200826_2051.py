# Generated by Django 3.1 on 2020-08-26 20:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0018_auto_20200826_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='operation_start',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 26, 20, 51, 57, 51959, tzinfo=utc), verbose_name='Inicio de operaciones'),
        ),
    ]