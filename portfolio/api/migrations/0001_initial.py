# Generated by Django 5.2 on 2025-04-17 14:24

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
                ('date_started', models.DateField(default=datetime.date.today)),
                ('date_completed', models.DateField(default=datetime.date.today)),
                ('program', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('degree', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=60)),
                ('role', models.CharField(max_length=60)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='skills/')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='api.experience')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('github_link', models.URLField(blank=True, null=True)),
                ('live_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('experience', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='api.experience')),
                ('skills', models.ManyToManyField(related_name='projects', to='api.skill')),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='experiences', to='api.skill'),
        ),
    ]
