from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now

# Create your models here.
class Bussiness(models.Model):
    key = models.SlugField(verbose_name='Clave', max_length=100, unique=True)
    name= models.CharField(max_length=100, verbose_name='Nombre')
    address= models.CharField(max_length=100, verbose_name='Direccion')
    phone= models.CharField(max_length=100, verbose_name='Telefono')
    email= models.CharField(max_length=100, verbose_name='Correo electrónico')
    
    

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresa'
        ordering = ['-name']

    def __str__(self):
        return self.name

class Comment (models.Model):
    email = models.CharField(max_length=100, verbose_name='Correo electrónico')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    content = RichTextField( verbose_name='Contenido')
    sended = models.DateTimeField(verbose_name='Fecha de envio', default=now)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-sended']

def __str__(self):
        return self.title