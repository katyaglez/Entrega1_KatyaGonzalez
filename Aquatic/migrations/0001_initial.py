# Generated by Django 4.1.5 on 2023-01-13 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('domicilio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('duracion', models.CharField(max_length=15)),
                ('maestro', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tamaño', models.CharField(max_length=30)),
                ('precio', models.CharField(max_length=30)),
            ],
        ),
    ]