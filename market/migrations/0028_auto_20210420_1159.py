# Generated by Django 3.1 on 2021-04-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0027_auto_20200828_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./staticfiles/market/img/company', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='company',
            name='product1',
            field=models.ImageField(blank=True, null=True, upload_to='./staticfiles/market/img/company', verbose_name='Producto 1'),
        ),
        migrations.AlterField(
            model_name='company',
            name='product2',
            field=models.ImageField(blank=True, null=True, upload_to='./staticfiles/market/img/company', verbose_name='Producto 2'),
        ),
        migrations.AlterField(
            model_name='company',
            name='product3',
            field=models.ImageField(blank=True, null=True, upload_to='./staticfiles/market/img/company', verbose_name='Producto 3'),
        ),
        migrations.AlterField(
            model_name='company',
            name='product4',
            field=models.ImageField(blank=True, null=True, upload_to='./staticfiles/market/img/company', verbose_name='Producto 4'),
        ),
        migrations.AlterField(
            model_name='company',
            name='product5',
            field=models.ImageField(blank=True, null=True, upload_to='./staticfiles/market/img/company', verbose_name='Producto 5'),
        ),
        migrations.AlterField(
            model_name='company',
            name='product6',
            field=models.ImageField(blank=True, null=True, upload_to='./staticfiles/market/img/company', verbose_name='Producto 6'),
        ),
    ]
