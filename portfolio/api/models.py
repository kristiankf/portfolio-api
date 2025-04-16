from datetime import date
from django.db import models

# Create your models here.
class Education(models.Model):
    institution = models.CharField(max_length=100)
    date_started = models.DateField(default=date.today)
    date_completed = models.DateField(default=date.today)
    program = models.CharField(max_length=200)
    description = models.TextField(max_length=200, blank=True)
    degree = models.CharField() 

    def __str__(self):
        return self.institution
    
class Skill(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='skills/', blank=True, null=True)

    def __str__(self):
        return self.nameß

class Experience(models.Model):
    company_name = models.CharField(max_length=60)
    role = models.CharField(max_length=60)
    description = models.TextField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name="experiences", blank=True)

    def __str__(self):
        return self.company_name

class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    skills = models.ManyToManyField(Skill, related_name="projects")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    experience = models.ForeignKey(Experience, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')

    def __str__(self):
        return self.title

class ContactForm(models.Model):
    name = models.CharField()
    email = models.EmailField()
    # subject = models.CharField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

    


