# Generated by Django 5.0.2 on 2024-03-21 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PNP', '0003_rename_user_id_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PNP.class'),
        ),
    ]
