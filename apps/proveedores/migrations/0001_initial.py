# Generated by Django 5.1.2 on 2025-04-22 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=20, unique=True)),
                ('num_contacto', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
