# Generated by Django 5.2 on 2025-04-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_skill_icon_name_alter_education_degree_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='location',
            field=models.CharField(blank=True, null=True),
        ),
    ]
