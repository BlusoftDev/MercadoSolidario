from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['-created']

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    preview = models.TextField( verbose_name='Texto en vista previa', default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam in nunc molestie purus viverra bibendum. Aliquam fermentum tellus nec consequat venenatis. Mauris vitae hendrerit nunc, a faucibus neque. Fusce et purus erat. Nunc pellentesque augue et laoreet accumsan. Proin dictum enim sapien, ut aliquet diam lobortis nec. Suspendisse id neque eu magna aliquet fermentum. Proin faucibus iaculis urna eget dignissim.' )
    content = RichTextField( verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorías')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')
    comments = models.IntegerField(default=0, editable=False, verbose_name='Comentarios')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title
