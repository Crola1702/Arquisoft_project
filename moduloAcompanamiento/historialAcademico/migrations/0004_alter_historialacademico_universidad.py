# Generated by Django 3.2.12 on 2022-04-07 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universidad', '0001_initial'),
        ('historialAcademico', '0003_auto_20220407_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialacademico',
            name='universidad',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='universidad.universidad'),
        ),
    ]
