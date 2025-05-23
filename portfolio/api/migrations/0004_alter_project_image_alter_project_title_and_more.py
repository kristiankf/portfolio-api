# Generated by Django 5.2 on 2025-04-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_experience_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='skills'),
        ),
    ]
