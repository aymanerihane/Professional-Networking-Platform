# Generated by Django 5.0.2 on 2024-03-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNP', '0014_comment_number_of_likes_comment_number_of_replies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='educations',
            field=models.JSONField(blank=True, default=list, max_length=100),
        ),
        migrations.AlterField(
            model_name='cv',
            name='experiences',
            field=models.JSONField(blank=True, default=list, max_length=100),
        ),
    ]