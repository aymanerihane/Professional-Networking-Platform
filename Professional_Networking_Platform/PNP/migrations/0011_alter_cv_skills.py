# Generated by Django 5.0.2 on 2024-03-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNP', '0010_alter_cv_educations_alter_cv_experiences_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='skills',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
