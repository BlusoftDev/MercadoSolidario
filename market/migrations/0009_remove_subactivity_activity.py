# Generated by Django 3.1 on 2020-08-18 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_subactivity_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subactivity',
            name='activity',
        ),
    ]