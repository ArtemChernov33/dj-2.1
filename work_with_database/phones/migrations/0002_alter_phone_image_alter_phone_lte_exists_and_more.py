# Generated by Django 4.0.4 on 2022-05-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(max_length=50),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.TextField(max_length=50),
        ),
    ]