# Generated by Django 4.0.1 on 2022-01-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='marcasvehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=25)),
                ('serie', models.CharField(max_length=25)),
                ('ano_fabricacion', models.IntegerField()),
                ('pais_fabricacion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_vendedor', models.CharField(max_length=35)),
                ('apellido_vendedor', models.CharField(max_length=35)),
                ('email_vendedor', models.EmailField(max_length=30)),
                ('sucursal', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehiculo_vendido', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('garantia_tiempo', models.IntegerField()),
                ('garantia_kilometros', models.IntegerField()),
            ],
        ),
    ]
