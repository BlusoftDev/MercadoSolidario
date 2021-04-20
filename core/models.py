from django.db import models

# Create your models here.
class Banner(models.Model):
    sld1 = models.ImageField(verbose_name='Slide 1', upload_to='./staticfiles/core/img/banner', null=True, blank=True)
    sld2 = models.ImageField(verbose_name='Slide 2', upload_to='./staticfiles/core/img/banner', null=True, blank=True)
    sld3 = models.ImageField(verbose_name='Slide 3', upload_to='./staticfiles/core/img/banner', null=True, blank=True)
    sld4 = models.ImageField(verbose_name='Slide 4', upload_to='./staticfiles/core/img/banner', null=True, blank=True)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'

    def __str__(self):
        return "Banner"