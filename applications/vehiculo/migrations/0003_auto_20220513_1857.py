# Generated by Django 3.0.6 on 2022-05-14 00:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_remove_transport_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('date', models.DateField(blank=True, null=True, verbose_name='fecha de creacion')),
                ('unit', models.CharField(choices=[('0', 'Unidades'), ('1', 'Quintales'), ('2', 'Toneladas')], max_length=1, verbose_name='unidad de medida')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.AlterModelOptions(
            name='transport',
            options={'verbose_name': 'Transporte', 'verbose_name_plural': 'Transportes'},
        ),
        migrations.CreateModel(
            name='Flete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date', models.DateField(blank=True, null=True, verbose_name='fehca de transaccion ')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='precio del flete')),
                ('description', models.TextField(blank=True, verbose_name='descripcion del viaje')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculo.Empresa')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculo.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
