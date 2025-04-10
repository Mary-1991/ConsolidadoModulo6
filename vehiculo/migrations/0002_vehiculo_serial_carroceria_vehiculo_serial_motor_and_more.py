# Generated by Django 5.1.3 on 2024-11-11 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='serial_carroceria',
            field=models.CharField(default='No especificado', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='serial_motor',
            field=models.CharField(default='No especificado', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='categoria',
            field=models.CharField(choices=[('Particular', 'Particular'), ('Comercial', 'Comercial'), ('Camión', 'Camión'), ('SUV', 'SUV')], max_length=50),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(choices=[('Ford', 'Ford'), ('Chevrolet', 'Chevrolet'), ('Toyota', 'Toyota'), ('Honda', 'Honda'), ('Nissan', 'Nissan')], max_length=50),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='modelo',
            field=models.CharField(max_length=50),
        ),
    ]
