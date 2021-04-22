from django.db import models
from .validators import validate_file_size

# Create your models here.
class Banner(models.Model):
    sld1 = models.ImageField(
        verbose_name='Slide 1', 
        upload_to='banner', 
        null=True, 
        blank=True, 
        validators=[validate_file_size], 
        default='banner/default/sld-1min.png',
    )
    sld2 = models.ImageField(
        verbose_name='Slide 2', 
        upload_to='banner', 
        null=True, 
        blank=True, 
        validators=[validate_file_size], 
        default='banner/default/sld2min.png',
    )
    sld3 = models.ImageField(
        verbose_name='Slide 3', 
        upload_to='banner', 
        null=True, 
        blank=True, 
        validators=[validate_file_size], 
        default='banner/default/sld1min.png',
    )
    sld4 = models.ImageField(
        verbose_name='Slide 4', 
        upload_to='banner', 
        null=True, 
        blank=True, 
        validators=[validate_file_size], 
        default='banner/default/sld3.png',
    )

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'

    def __str__(self):
        return "Banner"