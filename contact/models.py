from django.db import models

# Create your models here.
class Bussiness(models.Model):
    key = models.SlugField(verbose_name='Clave', max_length=100, unique=True)
    name= models.CharField(max_length=100, verbose_name='Nombre')
    address= models.CharField(max_length=100, verbose_name='Direccion')
    phone= models.CharField(max_length=100, verbose_name='Telefono')
    email= models.CharField(max_length=100, verbose_name='Correo electrónico')
    phrase= models.TextField(max_length=100, verbose_name='Frase')
    

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresa'
        ordering = ['-name']

    def __str__(self):
        return self.name