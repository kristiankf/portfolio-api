from .models import Education, Experience, Project, ExperienceDescription, Skill, ContactForm
from .serializers import EducationSerializer, ExperienceSerializer, ProjectSerializer, ExperienceDescriptionSerializer, SkillSerializer, ContactFormSerializer
from rest_framework import generics

# Create your views here.
#create list update delete
class EducationList(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class EducationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ExperienceList(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ExperienceDescriptionList(generics.ListCreateAPIView):
    queryset = ExperienceDescription.objects.all()
    serializer_class = ExperienceDescriptionSerializer

class ExperienceDescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExperienceDescription.objects.all()
    serializer_class = ExperienceDescriptionSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ContactFormList(generics.ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

class ContactFormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
