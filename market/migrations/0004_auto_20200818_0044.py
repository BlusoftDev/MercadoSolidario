# Generated by Django 3.1 on 2020-08-18 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20200818_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Método de pago',
                'verbose_name_plural': 'Métodos de pago',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='SubActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Método de pago',
                'verbose_name_plural': 'Métodos de pago',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='company',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.activity', verbose_name='Actividad'),
        ),
        migrations.AlterField(
            model_name='company',
            name='subactivity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.subactivity', verbose_name='Actividad especifica'),
        ),
    ]