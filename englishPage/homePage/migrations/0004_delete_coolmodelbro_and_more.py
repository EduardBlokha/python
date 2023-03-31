# Generated by Django 4.1.7 on 2023-02-28 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0003_coolmodelbro_alter_postmodel_mark_of_translate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CoolModelBro',
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='mark_of_translate',
            field=models.CharField(choices=[('FR', 'A'), ('SO', 'B'), ('JR', 'C'), ('SR', 'D'), ('GR', 'E')], default='FR', max_length=2),
        ),
    ]
