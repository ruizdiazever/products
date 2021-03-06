from django.db import models

class Producto(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    #image = models.ImageField()
    description = models.TextField(help_text="Descripcion del producto")
    stock = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    # Definimos el metodo string para que por consola devuelva una cadena.
    def __str__(self):
        return self.name