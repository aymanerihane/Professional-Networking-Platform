# Generated by Django 5.0.2 on 2024-03-26 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PNP', '0034_remove_post_link_remove_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friends_request',
        ),
    ]
