# Generated by Django 4.2.6 on 2023-11-13 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_alter_project_managers_project_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
