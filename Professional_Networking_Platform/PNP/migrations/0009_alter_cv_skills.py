# Generated by Django 5.0.2 on 2024-03-21 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNP', '0008_remove_comment_objects_id_comment_object_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='skills',
            field=models.JSONField(blank=True, default=dict, max_length=100),
        ),
    ]