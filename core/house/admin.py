from django.contrib import admin
from . import models

admin.site.register(models.Coin)
admin.site.register(models.Characteristic)
admin.site.register(models.CharacteristicHouse)
admin.site.register(models.Cost)
admin.site.register(models.House)
