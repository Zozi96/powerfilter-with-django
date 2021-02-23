from django.contrib import admin
from .models import Cine, Movie

admin.site.register(Cine, Movie)
