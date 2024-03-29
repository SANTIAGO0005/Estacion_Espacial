from django.db import models
from pydoc import describe

# Create your models here.
class Categoria(models.Model):
    """Model definition for Categoria."""
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['descripcion']

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.descripcion



    # Create your models here.
class Nave(models.Model):
    """Model definition for Nave."""

    # TODO: Define fields here
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    anio_fabricacion = models.IntegerField()
    peso = models.IntegerField()
    numero_motores = models.IntegerField()
    numero_tripulantes = models.IntegerField()
    potencia = models.IntegerField()
    objetivo = models.CharField(max_length=50)
    capacidad_carga = models.IntegerField()
    activo = models.BooleanField(default=True)
    combustible = models.CharField(max_length=50,blank=True)


    class Meta:
        """Meta definition for Nave."""

        verbose_name = 'Nave'
        verbose_name_plural = 'Naves'

    def __str__(self):
        """Unicode representation of Nave."""
        return'{}'.format(self.nombre, self.modelo, self.fabricante, self.categoria, self.anio_fabricacion, self.peso, self.numero_motores)

    
class Inventario(models.Model):
    """Model definition for Inventario."""
    nave = models.ForeignKey(Nave, on_delete=models.CASCADE)
 
    cantidad = models.IntegerField()

    class Meta:
        """Meta definition for Inventario."""

        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'

    def __str__(self):
        """Unicode representation of Inventario."""
        return'{}'.format(self.nave, self.cantidad)