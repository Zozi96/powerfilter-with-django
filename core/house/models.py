from django.db import models


class Characteristic(models.Model):
    name = models.CharField(max_length=50, unique=True)
    countable = models.BooleanField(default=False)

    class Meta:
        db_table = 'caracteristica'
        verbose_name = 'Característica'
        verbose_name_plural = 'Características'

    def __str__(self):
        return str(self.name)


class Coin(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)

    class Meta:
        db_table = 'moneda'
        verbose_name = 'Moneda'
        verbose_name_plural = 'Monedas'

    def __str__(self):
        return f'{self.name} - {self.abbreviation}'


class House(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        db_table = 'casa'
        verbose_name = 'House'
        verbose_name_plural = 'Houses'

    def __str__(self):
        return str(self.title)


class CharacteristicHouse(models.Model):
    house = models.OneToOneField(House, on_delete=models.CASCADE)
    characteristics = models.ManyToManyField(Characteristic)
    quantity = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        db_table = 'caracteristica_casa'
        verbose_name = 'CharacteristicHouse'
        verbose_name_plural = 'CharacteristicHouses'

    def __str__(self):
        return f'{self.house}'


class Cost(models.Model):
    house = models.OneToOneField(House, on_delete=models.CASCADE)
    cost_of_sale = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    rental_cost = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'costo'
        verbose_name = 'Cost'
        verbose_name_plural = 'Costs'

    def __str__(self):
        if self.cost_of_sale is None:
            self.cost_of_sale = ''
        elif self.rental_cost is None:
            self.rental_cost = ''
        return f'{self.cost_of_sale} {self.rental_cost}'
