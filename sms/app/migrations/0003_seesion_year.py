# Generated by Django 3.0.5 on 2023-08-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230803_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seesion_Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start', models.CharField(max_length=100)),
                ('session_end', models.CharField(max_length=100)),
            ],
        ),
    ]
