# Generated by Django 4.2.6 on 2023-11-03 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-start_date',)},
        ),
        migrations.AlterField(
            model_name='vote',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='projects.project'),
        ),
    ]