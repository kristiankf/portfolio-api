from rest_framework import serializers
from .models import Experience, Project, Skill, ExperienceDescription, ContactForm, Education
from cloudinary.utils import cloudinary_url

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
    logo_url = serializers.SerializerMethodField()
    class Meta:
        model = Skill
        fields = '__all__'

    def get_logo_url(self, obj):
        if obj.logo:
            url, options = cloudinary_url(obj.logo.public_id)
            return url
        return None

# this one is to just get something in the project
class SimpleExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'company_name', 'role']


class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    experience = SimpleExperienceSerializer(read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'skills',
            'image', 'github_link', 'live_link', 'created_at', 'experience', 'image_url'
        ]
    
    def get_image_url(self, obj):
        if obj.image:
            url, options = cloudinary_url(obj.image.public_id)
            return url
        return None

class ExperienceSerializer(serializers.ModelSerializer):
    projects =  ProjectSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    descriptions = ExperienceDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = ["id", "company_name", "role", "start_date", "end_date", "skills", "descriptions", "projects", "location", "link"]

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['id', 'name', 'email', 'message', 'submitted_at']