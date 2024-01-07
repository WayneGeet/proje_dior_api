# Generated by Django 4.2.6 on 2023-11-13 07:15

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_project_about_project_project_type'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='project',
            managers=[
                ('approved_projects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='approved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
