# Generated by Django 5.0.2 on 2024-03-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNP', '0020_alter_user_cv_alter_user_photo_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cv',
            field=models.FileField(blank=True, default='cv_default.jpg', null=True, upload_to='cv/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo_profile',
            field=models.FileField(blank=True, default='default.jpg', null=True, upload_to='avatar/'),
        ),
    ]
