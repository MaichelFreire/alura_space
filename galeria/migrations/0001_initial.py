# Generated by Django 4.2.1 on 2023-06-16 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('foto', models.CharField(max_length=100)),
            ],
        ),
    ]
