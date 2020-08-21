from django.db import models
from taggit.managers import TaggableManager


DELIVERY = (
        ('N', 'Colonias cercanas'),
        ('C', 'Toda la ciudad'),
        ('O', 'Otras ciudades'),

    )

# Create your models here.
class Payment(models.Model):
    name= models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Método de pago'
        verbose_name_plural = 'Métodos de pago'
        ordering = ['-created']

    def __str__(self):
        return self.name

class Activity(models.Model):
    name= models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Actividad económica'
        verbose_name_plural = 'Actividades económica'
        ordering = ['-created']

    def __str__(self):
        return self.name

class SubActivity(models.Model):
    name= models.CharField(max_length=100, verbose_name='Nombre')
    activity= models.ForeignKey(Activity, verbose_name='Actividad',on_delete=models.CASCADE, default='Servicios')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Subactividad'
        verbose_name_plural = 'Subactividades'
        ordering = ['-created']

    def __str__(self):
        return self.name


class City(models.Model):
    name= models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        ordering = ['-created']

    def __str__(self):
        return self.name
        
    
class Locality(models.Model):
    name= models.CharField(max_length=100, verbose_name='Nombre')
    city= models.ForeignKey(City, verbose_name='Municipio',on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        ordering = ['-created']

    def __str__(self):
        return self.name

class Colony(models.Model):
    locality= models.ForeignKey(Locality, verbose_name='Localidad',on_delete=models.CASCADE)
    name= models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Colonia'
        verbose_name_plural = 'Colonias'
        ordering = ['-created']

    def __str__(self):
        return self.name

class Company(models.Model):
    name= models.CharField(max_length=100, verbose_name='Nombre', )
    city= models.ForeignKey(City, verbose_name='Municipio' ,on_delete=models.CASCADE, default=2)
    locality= models.ForeignKey(Locality, verbose_name='Localidad',on_delete=models.CASCADE, default=2)
    postal_code= models.CharField(max_length=100, verbose_name='Código postal')
    colony= models.ForeignKey(Colony, verbose_name='Colonia',on_delete=models.CASCADE, default=2)
    street= models.CharField(max_length=100, verbose_name='Calle', blank=True, null=True)
    ext_number= models.CharField(max_length=100, verbose_name='Número exterior', blank=True, null=True)
    int_number= models.CharField(max_length=100, verbose_name='Número interior', blank=True, null=True)
    to_home= models.BooleanField (verbose_name='Servicio a domicilio', blank=True, null=True)
    delivery_options= models.CharField(max_length=1, verbose_name='Entrega en:', choices=DELIVERY, blank=True, null=True)
    platform = models.CharField(max_length=300, verbose_name='Url Plataforma' , null=True, blank=True)
    phone= models.CharField(max_length=100, verbose_name='Telefono', null=True, blank=True)
    cellphone= models.CharField(max_length=100, verbose_name='Telefono Móvil')
    email= models.CharField(max_length=100, verbose_name='Correo electrónico', null=True, blank=True)
    activity = models.ForeignKey(Activity, verbose_name='Actividad' ,on_delete=models.CASCADE, default=2,  null=True, blank=True)
    subactivity = models.ForeignKey(SubActivity, verbose_name='Actividad especifica' ,on_delete=models.CASCADE, default=2, null=True, blank=True)
    tags = TaggableManager()
    payment_method = models.ManyToManyField(Payment, verbose_name='Metodo de pago')
    image = models.ImageField(verbose_name='Imagen', upload_to='market', null=True, blank=True)
    let_me_know_more = models.BooleanField (verbose_name='Desea contarnos mas', null=True, blank=True)
    join = models.BooleanField (verbose_name='Quiere se parte', null=True, blank=True)
    lat = models.FloatField(verbose_name='Latitud', default=0.0)
    long = models.FloatField(verbose_name='Longitud', default=0.0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')

    class Meta:
        verbose_name = 'Empresa sonorense'
        verbose_name_plural = 'Empresas sonorenses'
        ordering = ['-created']

    def __str__(self):
        return self.name

    
