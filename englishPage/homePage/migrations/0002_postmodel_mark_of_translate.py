# Generated by Django 4.1.7 on 2023-02-28 22:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='mark_of_translate',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
