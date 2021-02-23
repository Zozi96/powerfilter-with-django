# Generated by Django 3.2b1 on 2021-02-23 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del cine')),
            ],
            options={
                'db_table': 'cine',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Pelicula')),
                ('hour', models.TimeField(verbose_name='Hora')),
                ('cine', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cinema.cine')),
            ],
            options={
                'db_table': 'pelicula',
            },
        ),
    ]
