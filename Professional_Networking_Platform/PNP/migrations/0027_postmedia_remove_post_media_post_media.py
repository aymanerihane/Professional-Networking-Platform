# Generated by Django 5.0.2 on 2024-03-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNP', '0026_remove_cv_introduction'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='media',
        ),
        migrations.AddField(
            model_name='post',
            name='media',
            field=models.ManyToManyField(blank=True, related_name='posts', to='PNP.postmedia'),
        ),
    ]