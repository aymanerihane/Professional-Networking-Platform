# Generated by Django 5.0.3 on 2024-03-25 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNP', '0030_remove_class_description_remove_class_section_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
