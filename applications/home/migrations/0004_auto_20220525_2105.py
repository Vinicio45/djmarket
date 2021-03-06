# Generated by Django 3.0.6 on 2022-05-26 03:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220523_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.TextField(blank=True, verbose_name='asunto de la reunion')),
            ],
            options={
                'verbose_name': 'grupo',
                'verbose_name_plural': 'Grupos',
            },
        ),
        migrations.AlterField(
            model_name='meet',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Group'),
        ),
    ]
