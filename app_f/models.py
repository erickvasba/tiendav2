from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser, User

# CLOUDINARY
from cloudinary.models import CloudinaryField
import cloudinary.uploader

# Create your models here.


class Profile(models.Model):
    CHOICES_CIUDAD = (
        ('La paz', 'La Paz'),
        ('El Alto', 'El Alto'),
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    celular = models.CharField('Celular', max_length=50, default='0')
    direccion = models.CharField('Dirección', max_length=150, default='')
    ciudad = models.CharField('Ciudad', max_length=50,
                              choices=CHOICES_CIUDAD, default='La Paz')

    def __str__(self):
        return self.celular


class Producto(models.Model):
    producto_nombre = models.CharField('Nombre Producto', max_length=50)
    producto_marca = models.CharField(
        'Marca Producto', max_length=50, blank=True)
    producto_modelo = models.CharField(
        'Modelo Producto', max_length=50, blank=True)
    producto_precio = models.CharField(
        'Precio Producto', max_length=50, blank=True)
    producto_calificacion = models.CharField(
        'Calificacion Producto', max_length=50, default='Bueno')
    producto_fecha_creacion = models.DateField(
        'Fecha Creación', auto_now=True)

    def __str__(self):
        return self.producto_nombre

    def get_absolute_url(self):
        return reverse("producto-detalle", kwargs={"pk": self.pk})


class Carrito(models.Model):
    carrito_fecha_creacion = models.DateField(auto_now=True)
    carrito_vendido = models.BooleanField(default=False)
    carrito_estado = models.CharField('Carrito Estado', max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto, through='Carrito_has_Producto')


class Carrito_has_Producto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.CharField('Cantidad', max_length=50)


class Foto_producto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    foto_foto = models.ImageField(
        'Producto Foto', upload_to='fotos/productos/', default='fotos/productos/none.jpeg')
    foto_foto2 = CloudinaryField('image')

    foto_descripcion = models.CharField(
        'Descripcion', max_length=50, default="")
    foto_fecha_creacion = models.DateField('Fecha Creación', auto_now=True)

    def save(self, *args, **kwargs):
        cloudinary.uploader.upload(self.foto_foto, use_filename=True)
        super(Foto_producto, self).save(*args, **kwargs)


class Promocion(models.Model):
    promocion_nombre = models.CharField('Nombre Promoción', max_length=50)
    promocion_descripcion = models.CharField('Descripción', max_length=150)
    promocion_fecha_creacion = models.CharField(
        'Fecha Creación', max_length=50)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.promocion_nombre


class Venta(models.Model):
    venta_costo_total = models.CharField('Costo Total', max_length=50)
    venta_fecha_venta = models.DateField('Fecha Venta', auto_now=True)
    carrito = models.OneToOneField(Carrito, on_delete=models.CASCADE)

    def __str__(self):
        return self.carrito
