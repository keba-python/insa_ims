# Generated by Django 4.1.2 on 2022-11-05 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Stationary', 'Stationary'), ('Electronics', 'Electronics'), ('Food', 'Food'), ('other', 'other')], max_length=20, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
