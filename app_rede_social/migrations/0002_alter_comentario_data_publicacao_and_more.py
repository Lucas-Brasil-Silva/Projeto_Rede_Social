# Generated by Django 4.2.7 on 2023-11-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_rede_social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data_publicacao',
            field=models.DateTimeField(default='22-11-2023 às 17:11'),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default='22-11-2023 às 17:11'),
        ),
    ]
