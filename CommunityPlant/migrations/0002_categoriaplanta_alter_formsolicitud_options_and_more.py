# Generated by Django 4.0.4 on 2022-06-17 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CommunityPlant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPlanta',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id categoria')),
                ('nombreCategoria', models.CharField(max_length=40, unique=True, verbose_name='Nombre categoria')),
            ],
            options={
                'verbose_name_plural': 'CategoriaPlanta',
            },
        ),
        migrations.AlterModelOptions(
            name='formsolicitud',
            options={'verbose_name_plural': 'FormSolicitud'},
        ),
        migrations.CreateModel(
            name='CatalogoPlantas',
            fields=[
                ('idPlanta', models.AutoField(primary_key=True, serialize=False, verbose_name='Id planta')),
                ('nombrePlanta', models.CharField(max_length=30, unique=True, verbose_name='Nombre planta')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CommunityPlant.categoriaplanta')),
            ],
            options={
                'verbose_name_plural': 'nombrePlanta',
            },
        ),
    ]