# Generated by Django 3.2.6 on 2022-04-06 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manejadorDeCitas', '0001_initial'),
        ('reporte', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='citas',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='manejadorDeCitas.cita'),
            preserve_default=False,
        ),
    ]
