# Generated by Django 3.2b1 on 2021-02-24 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('countable', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Característica',
                'verbose_name_plural': 'Características',
                'db_table': 'caracteristica',
            },
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Moneda',
                'verbose_name_plural': 'Monedas',
                'db_table': 'moneda',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'House',
                'verbose_name_plural': 'Houses',
                'db_table': 'casa',
            },
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_of_sale', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('rental_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('house', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='house.house')),
            ],
            options={
                'verbose_name': 'Cost',
                'verbose_name_plural': 'Costs',
                'db_table': 'costo',
            },
        ),
        migrations.CreateModel(
            name='CharacteristicHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('characteristics', models.ManyToManyField(to='house.Characteristic')),
                ('house', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='house.house')),
            ],
            options={
                'verbose_name': 'CharacteristicHouse',
                'verbose_name_plural': 'CharacteristicHouses',
                'db_table': 'caracteristica_casa',
            },
        ),
    ]
