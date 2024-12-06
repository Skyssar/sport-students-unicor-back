# Generated by Django 5.1.3 on 2024-12-06 16:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.FloatField()),
                ('weight', models.FloatField()),
                ('imc', models.FloatField()),
                ('masa_muscular', models.FloatField()),
                ('masa_grasa', models.FloatField()),
                ('grasa_visceral', models.FloatField()),
                ('edad_metabolica', models.SmallIntegerField()),
                ('masa_osea', models.FloatField()),
                ('leger_file', models.FileField(upload_to='files')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='physical_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.PositiveBigIntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('typeId', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('TI', 'Tarjeta de identidad'), ('CE', 'Cédula de extranjería'), ('PS', 'Pasaporte')], max_length=2)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1)),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.PositiveBigIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
        migrations.CreateModel(
            name='SportHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.SmallIntegerField()),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sport', to='sport_students.sport')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SportHistoryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intercolegiados', models.BooleanField(default=False)),
                ('inter_fase', models.CharField(blank=True, max_length=200, null=True)),
                ('associated', models.BooleanField(default=False)),
                ('assoc_fase', models.CharField(blank=True, max_length=200, null=True)),
                ('merito_file', models.FileField(blank=True, null=True, upload_to='files')),
                ('anamnesis_file', models.FileField(upload_to='files')),
                ('ci_file', models.FileField(upload_to='files')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sport_history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]