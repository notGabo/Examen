# Generated by Django 4.0.4 on 2022-06-19 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommunityPlant', '0003_alter_catalogoplantas_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalogoplantas',
            options={'verbose_name_plural': 'CatalogoPlantas'},
        ),
        migrations.AddField(
            model_name='catalogoplantas',
            name='descripcionPlanta',
            field=models.CharField(blank=True, max_length=500, verbose_name='Descripcion planta'),
        ),
    ]