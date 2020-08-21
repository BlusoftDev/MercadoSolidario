# Generated by Django 3.1 on 2020-08-18 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_remove_subactivity_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='subactivity',
            name='activity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='market.activity', verbose_name='Actividad'),
        ),
    ]