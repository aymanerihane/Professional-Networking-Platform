# Generated by Django 5.0.2 on 2024-03-21 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNP', '0011_alter_cv_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cv',
            field=models.FileField(blank=True, default='cv_default.jpg', null=True, upload_to='media/cv/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo_profile',
            field=models.FileField(blank=True, default='pdp_default.jpg', null=True, upload_to='media/avatar/'),
        ),
    ]
