# Generated by Django 5.0.3 on 2024-03-25 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNP', '0031_alter_cours_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='Degree',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='class',
            name='Name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cours',
            name='class_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cours',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cours',
            name='salle',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='cours',
            name='subject',
            field=models.CharField(default='', max_length=100),
        ),
    ]
