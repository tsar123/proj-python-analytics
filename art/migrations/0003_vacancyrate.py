# Generated by Django 4.1.2 on 2023-01-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_geography'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=40)),
                ('rate', models.CharField(max_length=10)),
            ],
        ),
    ]