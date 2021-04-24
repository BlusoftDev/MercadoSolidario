from django.db import models
from .formatChecker import ContentTypeRestrictedFileField

# Create your models here.
class Banner(models.Model):
    sld1 = ContentTypeRestrictedFileField(
        verbose_name='Slide 1', 
        upload_to='banner', 
        null=True, 
        blank=True, 
        max_upload_size=1048576,
        content_types=['image/jpg', 'image/jpeg', 'image/png', 'image/jiff'],
        default='banner/default/sld-1min.png',
    )
    sld2 = ContentTypeRestrictedFileField(
        verbose_name='Slide 2', 
        upload_to='banner', 
        null=True, 
        blank=True, 
        max_upload_size=1048576,
        content_types=['image/jpg', 'image/jpeg', 'image/png', 'image/jiff'], 
        default='banner/default/sld2min.png',
    )
    sld3 = ContentTypeRestrictedFileField(
        verbose_name='Slide 3', 
        upload_to='banner', 
        null=True, 
        blank=True, 
        max_upload_size=1048576,
        content_types=['image/jpg', 'image/jpeg', 'image/png', 'image/jiff'], 
        default='banner/default/sld1min.png',
    )
    sld4 = ContentTypeRestrictedFileField(
        verbose_name='Slide 4', 
        upload_to='banner', 
        null=True, 
        blank=True, 
        max_upload_size=1048576,
        content_types=['image/jpg', 'image/jpeg', 'image/png', 'image/jiff'],
        default='banner/default/sld3.png',
    )

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'

    def __str__(self):
        return "Banner"