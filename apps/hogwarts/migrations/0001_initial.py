# Generated by Django 5.0.4 on 2024-04-10 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fundador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('animal', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('fundadorCasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hogwarts.fundador')),
            ],
        ),
    ]
