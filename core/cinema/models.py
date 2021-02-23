from django.db import models


class Cine(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del cine')

    class Meta:
        db_table = 'cine'

    def __str__(self):
        return str(self.name)


class Movie(models.Model):
    cine = models.OneToOneField(Cine, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Pelicula')
    hour = models.TimeField(verbose_name='Hora')

    class Meta:
        db_table = 'pelicula'

    def __str__(self):
        return str(self.name)
