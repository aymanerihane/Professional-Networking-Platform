# Generated by Django 5.0.2 on 2024-03-26 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNP', '0036_friendrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmedia',
            name='type',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
