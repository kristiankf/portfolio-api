from rest_framework import serializers
from .models import Experience, Project, Skill, ExperienceDescription, ContactForm, Education

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'id', 'institution', 'date_started', 'date_completed',
            'program', 'description', 'degree'
        ]

class ExperienceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceDescription
        fields = ['id', 'content']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

# this one is to just get something in the project
class SimpleExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'company_name', 'role']


class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    experience = SimpleExperienceSerializer(read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'skills',
            'image', 'github_link', 'live_link', 'created_at', 'experience'
        ]

class ExperienceSerializer(serializers.ModelSerializer):
    projects =  ProjectSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    descriptions = ExperienceDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = ["id", "company_name", "role", "start_date", "end_date", "skills", "descriptions", "projects", "location"]

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['id', 'name', 'email', 'message', 'submitted_at']