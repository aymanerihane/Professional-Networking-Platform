# Generated by Django 5.0.2 on 2024-03-27 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNP', '0037_postmedia_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participent',
            field=models.ManyToManyField(to='PNP.user'),
        ),
    ]
