# Generated by Django 4.2.6 on 2023-11-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_alter_project_managers_remove_project_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='projects'),
        ),
    ]
