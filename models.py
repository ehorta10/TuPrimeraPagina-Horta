from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    correo = models.EmailField()
    edad = models.IntegerField()
    intereses = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    cliente = models.CharField(max_length=40)
    producto = models.CharField(max_length=50)
    tienda = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cliente} - {self.producto}"