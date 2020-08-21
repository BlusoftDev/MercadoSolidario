# Generated by Django 3.1 on 2020-08-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='lat',
            field=models.FloatField(default=0.0, verbose_name='Latitud'),
        ),
        migrations.AddField(
            model_name='company',
            name='long',
            field=models.FloatField(default=0.0, verbose_name='Longitud'),
        ),
    ]